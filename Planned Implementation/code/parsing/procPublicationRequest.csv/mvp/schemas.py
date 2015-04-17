from schematics.models import Model, FieldDescriptor
from schematics.types import StringType, IntType
from schematics.types import DateTimeType
from schematics.types.compound import ModelType


class NoticeType(Model):
    name = StringType()
    id = IntType()


class SectionName(Model):
    name = StringType()
    id = IntType()


class Organization(Model):
    classification = StringType()
    parent = IntType()
    identifier = StringType()
    name = StringType()


class Notice(Model):
    title = StringType()
    noticetype = ModelType(NoticeType)
    sectionName = ModelType(SectionName)
    publishingOrganization = ModelType(Organization)
    createdAt = DateTimeType()
    endDate = DateTimeType()
    startDate = DateTimeType()
    lastUpdatedAt = DateTimeType()
    printOut = StringType()
    otherInfo = StringType()

if __name__ == '__main__':
    org = Organization()
    org.classification = "Agency"
    org.identifier = "675"
    org.name = "Mayor's office of Contract Services"
    org.parent =  "Mayor's Office'"


    org.validate()
    print(org.get_mock_object().to_primitive())


