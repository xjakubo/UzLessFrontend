from ..backendrequest.backendrequest import Backend_Request

# TODO: Prepare search


class View_Service:
    def __init__(self):
        self.__context = {}

    def _getEntites(self, endpoint: str):
        entities = Backend_Request.getDataFromEndpoint(endpoint)
        return entities

    def prepareBasicPage(self, module: str, subpage_title="Page"):
        self.__context["module"] = module
        self.__context["subpage_title"] = subpage_title
        return self

    def prepareTableView(self, table_headers: list, data_endpoint: str):
        self.__context["entities"] = self._getEntites(data_endpoint)
        self.__context["table_titles"] = table_headers
        return self

    def prepareInsertForm(self, insert_form=None):
        if insert_form is None:
            raise Exception("insert_form is None!") 
        self.__context["form"] = insert_form
        return self

    def sortKeysByOrder(self, desired_key_order):
        if "entities" not in self.__context:
            raise Exception("entities is None!") 
        entities = self.__context["entities"]
        for index, entity in enumerate(entities):
            entities[index] = {key: entity[key] for key in desired_key_order}
        self.__context["entities"] = entities
        return self

    def getContext(self):
        return self.__context.copy()

    def concatDataFromOtherTable(
        self, id_column_to_replace, fk_column_to_replace, data_endpoint
    ):
        if self.__context.get("entities") is None:
            raise Exception("entities is None!") 
        entities = self.__context.get("entities")
        concated_entities = Backend_Request.concatDataFromOtherTable(
            entities, id_column_to_replace, fk_column_to_replace, data_endpoint
        )
        self.__context["entities"] = concated_entities
        return self
