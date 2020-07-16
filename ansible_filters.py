#!/usr/bin/python

'''
    Provides filters for use in Ansible

    Add in filters as methods of the class FilterModule, then return them in
      the dict returned by filters
'''

import json

class FilterModule():
    ''' Filters for Ansible '''

    def filters(self):
        ''' Provide filter(s) to Ansible  '''
        return {
            'json_to_csv': self.json_to_csv
            }

    def json_to_csv(self, json_as_string):
        '''
        Read json_as_string and prepare it to be saved as a csv file

        inputs:
            json_as_string: the query_result output of an Ansible
              postgresql_query module
        outputs:
            json_as_string converted to a string with columns and linefeeds by
              row

        example usage:
            - name: Write output to csv file
              copy:
                content: "{{ output.query_result | json_to_csv }}"
                dest: "{{ output_path }}"
              delegate_to: localhost
              when: output_path is defined

        '''
        my_json = json.loads(json_as_string)
        columns = my_json[0].keys()
        result = ','.join(columns) + '\n'
        for item in my_json:
            result += ','.join([str(item[col]) for col in columns]) + '\n'
        return result
