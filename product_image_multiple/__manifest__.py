# -*- coding: utf-8 -*-
###################################################################################
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'Product Multiple Images & Videos',
    'version': '13.0.1.0.0',
    'summary': """Add Multiple Images & YouTube into Your Products""",
    'description': """""",
    'category': 'Base',
    'author': 'Kreative',
    'website': "",
    'license': 'AGPL-3',

    'price': 20.0,
    'currency': 'USD',

    'depends': ['base', 'product'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
    'demo': [

    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
