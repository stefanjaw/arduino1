# -*- coding: utf-8 -*-
from odoo import http

import logging

log = logging.getLogger(__name__)


class Arduino(http.Controller):
    @http.route('/arduino/<string:data>/', auth='public', csrf=False)
    def object(self, data, **kw):

        log.info(1596946009)
        log.info("\n===DEB DATA====\n%s\n",data)
        http.Response.status = '200'
        return "A0=0&IO0=0&IO1=0&IO2=0&IO3=0&IO4=0&IO5=0&IO6=0&IO7=0&IO8=0&IO9=0"
        #return {'test':True}
        #return http.request.render(True)


# -*- coding: utf-8 -*-
# from odoo import http


# class Arduino(http.Controller):
#     @http.route('/arduino/arduino/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arduino/arduino/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arduino.listing', {
#             'root': '/arduino/arduino',
#             'objects': http.request.env['arduino.arduino'].search([]),
#         })

#     @http.route('/arduino/arduino/objects/<model("arduino.arduino"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arduino.object', {
#             'object': obj
#         })
