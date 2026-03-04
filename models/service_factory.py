class Service:
    def get_service_name(self):
        pass

class Electrician(Service):
    def get_service_name(self):
        return "Electrician"

class Plumber(Service):
    def get_service_name(self):
        return "Plumber"

class Cleaner(Service):
    def get_service_name(self):
        return "Cleaner"

class Painter(Service):
    def get_service_name(self):
        return "Painter"

class ServiceFactory:
    @staticmethod
    def create_service(service_type):
        services = {
            "Electrician": Electrician,
            "Plumber": Plumber,
            "Cleaner": Cleaner,
            "Painter": Painter
        }

        service_class = services.get(service_type)
        return service_class() if service_class else None
