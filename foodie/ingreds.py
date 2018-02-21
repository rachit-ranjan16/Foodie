from configparser import ConfigParser
import requests
import json
import os

R_ID = 'rId'
SORT = 'sort'
Q = 'q'
KEY = 'key'
GET_API_URL = 'get_api_url'
SEARCH_API_URL = 'search_api_url'
FOOD_2_FORK = 'food2fork'
API_KEY = 'api_key'
TRENDING = 'trending'
RATING = 'rating'
YES_LIST = ['y', 'yes', 'yep', 'yeah']
NO_LIST = ['n', 'no', 'nope']


class ingreds(object):
    """
    Command Line App to use Food2Fork's Search API through REST calls to fetch top recipe for the given ingredients and report missing ones
    """
    def __init__(self, ing_list=[]):
        """
        Initializes Config Parser for reading config properties
        Initializes ingredient list
        :param ing_list:
        """
        config_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +\
                         os.sep +\
                         'config' +\
                         os.sep +\
                         'appConfig.ini'
        self.config = ConfigParser()
        self.config.read(config_file)
        self.ing_list = ing_list

    def get_missing_ingreds(self):
        """
        Driver method
            - Fetches top receipes through GET call to Food2Fork Search Recipes for given ingredients
                - By trending at first
                - By ratings if above fails
            - Fetches top recipe details through GET call to Food2Fork

        :return:
        """
        self.get_ingreds()
        ing_str = self.get_pretty_ingred_str()
        # Search API Payload - sort by trending
        data = {KEY: self.config.get(FOOD_2_FORK, API_KEY),
                Q: ing_str,
                SORT: self.config.get(FOOD_2_FORK, TRENDING)}

        try:
            r = requests.get(self.config.get(FOOD_2_FORK, SEARCH_API_URL), params=data)
            if r.status_code != 200:
                print('[ERROR] Received %d from Food2Fork for Search API' % r.status_code)
                return
        except Exception as e:
            print('[ERROR]Failed to reach Food2Fork Exception=%r' % e.with_traceback())
            return

        if json.loads(r.text)['count'] == 0:
            print('\nNo Results found for Trending Search')
            if self.get_search_by_ratings_enabled():
                # Sort by top rated
                data[SORT] = self.config.get(FOOD_2_FORK, RATING)
                try:
                    r = requests.get(self.config.get(FOOD_2_FORK, SEARCH_API_URL), params=data)
                    if r.status_code != 200:
                        print('[ERROR] Received %d from Food2Fork for Search API' % r.status_code)
                        return

                except Exception as e:
                    print('[ERROR]Failed to reach Food2Fork Exception=%r' % e.with_traceback())
                    return
            else:
                print("Exiting")
                return

        response_json = json.loads(r.text)
        if response_json['count'] == 0:
            print('No Matching Recipes found for the provided ingredients')
            return

        tr_id = response_json['recipes'][0]['recipe_id']
        data = {KEY: self.config.get(FOOD_2_FORK, API_KEY),
                R_ID: tr_id}

        try:
            r = requests.get(self.config.get(FOOD_2_FORK, GET_API_URL), params=data)
            if r.status_code != 200:
                print('[ERROR] Received %d from Food2Fork for Get API' % r.status_code)
                return
        except Exception as e:
            print('[ERROR]Failed to reach Food2Fork Exception=%r' % e.with_traceback())
            return

        top_recipe = json.loads(r.text)
        self.print_missing_ingreds(self.find_missing_ingreds(top_recipe['recipe']['ingredients']),
                                   title=top_recipe['recipe']['title'])

    def get_search_by_ratings_enabled(self):
        """
        Takes Yes/No input from the user for fetching recipes by ratings
        Loops till a valid input is entered
        :return: Boolean value corresponding to choice
        """
        while True:
            choice = input("Do you want search by ratings? (Y/N)\n")
            if choice.lower() in NO_LIST:
                sch_by_ratings = False
                break
            elif choice.lower() in YES_LIST:
                sch_by_ratings = True
                break
            else:
                print("Wrong Input. Try Again..")
        return sch_by_ratings

    def find_missing_ingreds(self, all_ings):
        """
        Creates a dict out of list of all ingredients with True values
        Marks the ingredients in all_ings dict as False if user entered ingredient is its substring
        Ingredients marked False are not used for further comparisons
        :param all_ings:
        :return: Ingredient Dictionary with repeated ingredients marked False
        """
        all_ings_dict = {}
        for i in all_ings:
            all_ings_dict[i] = True
        for i in range(len(self.ing_list)):
            for key in all_ings_dict.keys():
                if all_ings_dict[key]:
                    if key.lower().find(self.ing_list[i].lower()) != -1:
                        all_ings_dict[key] = False
        return all_ings_dict

    def print_missing_ingreds(self, all_ings_dict, title):
        """
        Prints the top receipe title and the list of ingredients user was missing from the initial input
        :param all_ings_dict:
        :param top_recipe:
        :return: None
        """
        print('\nMissing Ingredients for\n%r' % title)
        for key in all_ings_dict.keys():
            if all_ings_dict[key]:
                print(key)

    def get_pretty_ingred_str(self):
        """
        Format ingredients into lowercase csv
        :return: pretty printed comma separated string of input ingredients
        """
        ingreds_str = ''
        for i in self.ing_list:
            ingreds_str += i.lower() + ','
        return ingreds_str[:-1]

    def get_ingreds(self):
        """
        Inputs csv ingredient list from the user
        Input loops till user is satisfied
        :return:
        """
        more_inp = True
        while more_inp:
            self.ing_list.append((input("Enter Ingredient(s) - separated by commas\n")).strip())
            while True:
                choice = input("Do you want to enter more Ingredients? (Y/N)\n")
                if choice.lower() in NO_LIST:
                    more_inp = False
                    break
                elif choice.lower() in YES_LIST:
                    break
                else:
                    print("Invalid Input. Try Again..")
        print("Fetching Trending Recipes on Food2Fork")


if __name__ == "__main__" :
    ingreds().get_missing_ingreds()
