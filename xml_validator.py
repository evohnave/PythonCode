# -*- coding: utf-8 -*-
"""
@author: EA Vanhove
"""

from dataclasses import dataclass
from pathlib import Path

from lxml import etree

@dataclass
class XmlValidator:
    '''
    Validates an xml file against a given schema.  The schema is derived from
      an Xml Schema Document (*.xsd) file.

    Input: xsd_path - string path to your xsd file

    Unintended consequences: also validates the xsd document... if it is not
      correct there will be XMLSchema* exceptions raised by lxml.
    '''
    xsd_path: str

    #pylint: disable=W0201
    # Checks for attributes defined outside of __init__
    def __post_init__(self) -> None:
        self._xsd_name = Path(self.xsd_path).name
        self._xml_schema_doc = etree.parse(self.xsd_path)
        self._xml_schema = etree.XMLSchema(self._xml_schema_doc)
    #pylint: enable=W0201

    @property
    def xsd_name(self) -> str:
        ''' Just the name of the xsd file '''
        return self._xsd_name
    @property
    def xml_schema(self) -> str:
        ''' The schema '''
        return self._xml_schema
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._xsd_name})"
    def validate(self, xml_path: str) -> bool:
        '''
        Performs the actual validation for the class.

        Input: xml+path - the path to your xml file which will be validated

        Output: True - valid -- or -- False - invalid
        '''
        xml_doc = etree.parse(xml_path)
        return self.xml_schema.validate(xml_doc)
