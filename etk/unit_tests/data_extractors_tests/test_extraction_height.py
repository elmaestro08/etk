# -*- coding: utf-8 -*-
import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from data_extractors import height_extractor
height_test_data = {
  "jsonlines": [{'text': '\n           \n \n \n \n \n Ethnicity: White \n \n \n \n Hair Color: Brunette \n \n \n \n Eye Color: Hazel \n \n \n \n Body Type: Curvy \n \n \n \n Bust: 34 C \n \n \n \n Height: 5\'4" \n \n \n \n Availability: Incall, Outcall \n', 'height': [{'context': {'start': 153, 'end': 156}, 'value': '5\'4"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 151, 'end': 156}, 'value': '5\'4"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Measurements: 105lbs 5\'2" 34c with a beautiful face', 'height': [{'context': {'start': 21, 'end': 24}, 'value': '5\'2"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': "I'm very petite gentlemen, standing at 5''1 and 105lbs. i have a 34c bust.", 'height': [{'context': {'start': 39, 'end': 43}, 'value': '5\'1"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': '24 years old, 5\'2" 105lbs , 32B ', 'height': [{'context': {'start': 14, 'end': 17}, 'value': '5\'2"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Chrystle Kims \n Age: 24 yrs \nMeasurements: 32" B natural, 23", 33" ( 81-58-84 ) \nHeight: 5\' 7" (170cm) \nWeight: 51kg (112lb) \n \n \n \n \n \n Brooke Montpellier \n Age: 22 yrs \nMeasurements: 32" A natural, 25", 36" (82 - 61 - 86) \nHeight: 5\' 9" (179cm) \nWeight: 57kg (130lb) \n \n \n \n \n \n', 'height': [{'context': {'start': 89, 'end': 93}, 'value': '5\' 7"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 96, 'end': 101}, 'value': '170', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 233, 'end': 237}, 'value': '5\' 9"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 240, 'end': 245}, 'value': '179', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 87, 'end': 93}, 'value': '5\' 7"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 231, 'end': 237}, 'value': '5\' 9"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Shaved completely \n \n \n Height \n 167 cm \n \n \n Weight \n 53 kg \n \n \n Bust-Waist-Hip \n 85-60-87 \n \n \n Cup size \n B \n \n \n', 'height': [{'context': {'start': 33, 'end': 39}, 'value': '167', 'metadata': {'unit': 'centimeter'}}]}, {'text': 'DETAIL   \n \n \n \n Age : \n  19 \n Height :  178 \n Weight :  55 \n  Breast :  90-60-90 \n', 'height': [{'context': {'start': 37, 'end': 44}, 'value': '178', 'metadata': {'unit': 'centimeter'}}]}, {'text': 'Nationality:   Thai   Statistics:   34C-26-36   Height:   155 cm   Weight:   47 Kg   Hair Colour:   Brown   ', 'height': [{'context': {'start': 58, 'end': 64}, 'value': '155', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 54, 'end': 64}, 'value': '155', 'metadata': {'unit': 'centimeter'}}]}, {'text': 'Travel: \n worldwide \n \n \n Weight: \n 117 lb (53 kg) \n \n \n Height: \n 5.5 ft (166 cm) \n \n \n Ethnicity: \n Indian \n', 'height': [{'context': {'start': 67, 'end': 74}, 'value': '5.5', 'metadata': {'unit': 'foot'}}, {'context': {'start': 75, 'end': 81}, 'value': '166', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 63, 'end': 74}, 'value': '5.5', 'metadata': {'unit': 'foot'}}]}, {'text': "Age: \n 24 \n \n \n Height: \n 272cm / 8'9\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd \n \n \n Weight: \n 55kg / 121lbs \n \n \n Body (cm): \n 36/32/34 \n", 'height': [{'context': {'start': 26, 'end': 31}, 'value': '272', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 34, 'end': 37}, 'value': '8\'9"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 22, 'end': 31}, 'value': '272', 'metadata': {'unit': 'centimeter'}}]}, {'text': 'Age: 23   Height: 169   Weight: 55   Hair: Brown', 'height': [{'context': {'start': 16, 'end': 21}, 'value': '169', 'metadata': {'unit': 'centimeter'}}]}, {'text': '\n TS RUBI: THE NAME SAYS IT ALL!  \n INCALL $250 OUTCALL $350 \n \n \n \n \n \n Gender \n Age \n Ethnicity \n Hair Color \n Eye Color \n Height \n Weight \n Measurements \n Affiliation \n Availability \n Available To \n \n \n \n \n Transsexual \n 27 \n Latino/Hispanic \n Brown \n Hazel \n 5\'5" \n 130 lb \n 34C - 28" - 34" \n ', 'height': [{'context': {'start': 263, 'end': 266}, 'value': '5\'5"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Age : \n 22 \n \n \n  Weight  : \n 53 \n \n \n  Height  : \n 5.7 \n \n \n', 'height': [{'context': {'start': 46, 'end': 55}, 'value': '5.7', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Breasts DD Eyes gray Height 1.52 Skin Tanned Weight 60', 'height': [{'context': {'start': 27, 'end': 32}, 'value': '1.52', 'metadata': {'unit': 'meter/centimeter'}}]}, {'text': '\n Height: \n \n5\'7" - 167 cm  \n \n \n Weight: \n \n150lbs - 60 kg  \n ', 'height': [{'context': {'start': 13, 'end': 16}, 'value': '5\'7"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 20, 'end': 26}, 'value': '167', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 8, 'end': 16}, 'value': '5\'7"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': "\n Height: \n 168cm / 5'5\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd \n \n \n Weight: \n 55kg / 121lbs \n ", 'height': [{'context': {'start': 12, 'end': 17}, 'value': '168', 'metadata': {'unit': 'centimeter'}}, {'context': {'start': 20, 'end': 23}, 'value': '5\'5"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 8, 'end': 17}, 'value': '168', 'metadata': {'unit': 'centimeter'}}]}, {'text': "\n \n Height: \r\n                          5'3''\r\n                       \n \n \n \n \n \n Weight: \r\n                          125 lbs\r\n                       \n \n \n \n \n \n", 'height': [{'context': {'start': 40, 'end': 43}, 'value': '5\'3"', 'metadata': {'unit': 'foot/inch'}}]}, {'text': 'Height \n 5ft 8in - 5 ft 11in \n \n \n Bust \n \n 42 in \n \n \n \n Breasts \n Large,', 'height': [{'context': {'start': 9, 'end': 16}, 'value': '5.0\'8"', 'metadata': {'unit': 'foot/inch'}}, {'context': {'start': 19, 'end': 24}, 'value': '5.0', 'metadata': {'unit': 'foot'}}]}, {'text': 'Im White and Dominican 5ft 115lbs 38c Cup Size, 24 inch waiste', 'height': [{'context': {'start': 23, 'end': 27}, 'value': '5.0', 'metadata': {'unit': 'foot'}}]}, {'text': 'I am 25 of age, stand 5ft5in, fair in complexion, Long hair', 'height': [{'context': {'start': 22, 'end': 28}, 'value': '5.0\'5"', 'metadata': {'unit': 'foot/inch'}}]}]
}


class TestHeightExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_height_extractor(self):
        data_lines = height_test_data['jsonlines']
        out_data_lines = list()
        for line in data_lines:
            extraction = height_extractor.extract(line['text'])
            self.assertEqual(extraction, line['height'])

if __name__ == '__main__':
    unittest.main()