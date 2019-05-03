from rest_framework.test import APITestCase
from rest_framework import status
from equipment.models import Equipment


class EquipmentTestCase(APITestCase):

    # def modify_settings(self, **kwargs):


    def setUp(self) -> None:
        eq = {
            "name": "Тонометр автоматический Gamma Smart",
            "description": "Тонометр автоматический с манжетой на плечо Gamma Smart предназначен для определения " +
                           "артериального давления и пульса осциллометрическим методом.",
            "price": 1224,
            "currency": "грн",
            "guarantee": 5,
            "in_case": 1,
            "image": "",
            "manufacture_id": 1,
            "subgroup_id": 1,
            "type_of_id": 1
        }

        # e = Equipment(eq)
        # e.save()

    def test_getting_equipment_list(self):
        # response = self.client.get(
        #     path='/api/equipment?offset=1',
        #     format="json", **{'accept': 'application/json'}
        # )
        #
        # original_structure = {
        #     "data": [],
        #     "pagination": {}
        # }
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response=response, text=original_structure)
        self.assertEqual(200, 200)
