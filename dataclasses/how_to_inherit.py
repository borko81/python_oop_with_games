from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class Name:
    name: str

    def __repr__(self):
        return self.name


@dataclass(order=True)
class Company:
    company_name: ClassVar[str] = 'Company'
    employes: list = field(default_factory=list)

    def show_employees(self):
        return [name.name for name in self.employes]


p1 = Name('One')
p2 = Name('Two')
p3 = Name('Three')

company = Company()
company.employes.append(p1)
company.employes.append(p2)
company.employes.append(p3)

print(company.show_employees())
