import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-contract",
    description="Meta package for oca-contract Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-contract',
        'odoo13-addon-contract_payment_mode',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
