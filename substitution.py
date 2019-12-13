from pymatgen import Structure
from pymatgen.transformations.standard_transformations import SubstitutionTransformation
from pymatgen.transformations.standard_transformations import OrderDisorderedStructureTransformation


structure = Structure.from_file("POSCAR")


substitution = SubstitutionTransformation({"Nb3+": {"Nb3+":0.5, "Fe3+":0.5}})

# substitution = SubstitutionTransformation([("Nb3+", "Fe3+")])


result = substitution.apply_transformation(structure)


order = OrderDisorderedStructureTransformation(algo=2)

#print(order)
ResultOrder = order.apply_transformation(result, return_ranked_list=True)

print(ResultOrder)

for i, item in enumerate(ResultOrder):
    item['structure'].to(filename="POSCAR{:02d}".format(i))
#ResultOrder[0]['structure'].to(filename="POSCAR1")

