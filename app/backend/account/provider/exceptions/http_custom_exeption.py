from fastapi import HTTPException


class HttpCustomExceptions:
    provider = 1

    def service_connection_exception(self):
        return HTTPException(status_code=500, detail=f'provider: {self.provider} service connection error')

    def service_error(self, resp):
        error_mess = resp.json().get('detail')
        return HTTPException(status_code=500, detail=f'provider: {self.provider} service_message: {error_mess}')
