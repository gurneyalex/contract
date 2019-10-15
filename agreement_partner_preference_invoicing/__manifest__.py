# Copyright 2019 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Agreement Partner Preferences: Invoiceing",
    "summary": "Manage Partner Preferences about Invoicing in agreements",
    "version": "12.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Alpha",
    "category": "Sale",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["gurneyalex"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "agreement_sale_condition_base",
    ],
    "data": [
        'data/agreement.parameter.value.csv',
        "views/agreement.xml",
    ],
}
