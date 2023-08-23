import dash_bootstrap_components as dbc


# a function define a navbar
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Page 1", href="/page-1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page-2")),
        ],
        brand="Dash Bootstrap Components",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar
