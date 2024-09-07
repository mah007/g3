# -*- coding: utf-8 -*-
from odoo import http,_
from odoo.http import request
import werkzeug
from werkzeug.wrappers import Request, Response
import json



class Estate(http.Controller):
    @http.route(['/estate/properties','/estate/properties/<int:prop_id>'], auth='public',method=['GET','POST'],csrf=False)
    def index(self,prop_id = False, **kw):
        if prop_id:
            properties = request.env['estate.property'].sudo().search([('id', '=', prop_id)])
        else:
            properties = request.env['estate.property'].sudo().search([('active', '=', True)])
        vals =[]
        for prop in properties:
            val = {
                'prop_id': prop.id,
                'name': prop.name,
                'type': prop.property_type_id.name,
                'selling_price': prop.selling_price,
                'total_area': prop.total_area,
                'price_per_m': prop.price_per_m,
                'status': prop.state,

            }
            vals.append(val)

        headers = {'Content-Type': 'application/json'}
        return Response(
            json.dumps({"properties":vals}, indent=2),
            headers=headers)

    @http.route(['/estate/template',], auth='public', method=['GET', 'POST'], csrf=False, website=True)
    def template(self, **kw):
        values={}
        properties = request.env['estate.property'].sudo().search([('active', '=', True)])
        count = request.env['estate.property'].sudo().search_count([('active', '=', True)])

        values.update({
            'properties':properties,
            'count':count
        })
        print(values)

        return request.render('estate.web_template',values)

    @http.route(['/estate/template/prop/<int:prop_id>', ], auth='public', method=['GET', 'POST'], csrf=False, website=True)
    def template_prop_id(self, prop_id, **kw):
        values={}
        property1 = request.env['estate.property'].sudo().search([('id', '=', prop_id)])

        values.update({
            'properties':property1,
        })
        print(values)

        return request.render('estate.web_template_property', values)







