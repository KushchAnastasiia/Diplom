from equipment.serializers import *
from equipment.models import *


def get_full_equipment_data(d=None):
    ctx = d

    type_of = TypeSerializer(
        Type.objects.filter(id=int(d["type_of"])).first()).data

    manufacture = ManufacturerSerializer(
        Manufacturer.objects.filter(id=int(d["manufacture"])).first()).data

    country = CountrySerializer(
        Country.objects.filter(id=int(manufacture["country"])).first()
    ).data

    manufacture['country'] = country

    subgroup = SubGroupSerializer(
        SubGroup.objects.filter(id=int(d["subgroup"])).first()).data

    group = GroupSerializer(
        Group.objects.filter(id=int(subgroup["id"])).first()).data
    
    subgroup['group'] = group

    market_list = []
    market_id_list = EquipmentMarketConnection.objects.filter(equipment=d['id']).all()

    for x in market_id_list:
        market_list.append(
            MarketSerializer(x.market).data)

    ctx['type_of'] = type_of
    ctx['manufacture'] = manufacture
    ctx['subgroup'] = subgroup
    # ctx['group'] = group
    # ctx['country'] = country
    ctx['markets'] = market_list

    return ctx
