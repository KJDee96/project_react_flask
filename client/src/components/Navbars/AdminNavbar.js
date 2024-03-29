/*!

=========================================================
* Argon Dashboard React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
import {Link} from "react-router-dom";
import {deleteTokens, getToken} from "authHelpers";
// reactstrap components
import {
    Alert,
    DropdownMenu,
    DropdownItem,
    UncontrolledDropdown,
    DropdownToggle,
    Form,
    FormGroup,
    InputGroupAddon,
    InputGroupText,
    Input,
    InputGroup,
    Navbar,
    Nav,
    Container,
    Media
} from "reactstrap";
import axios from "axios";

class AdminNavbar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: true,
            user: ''
        };
    }

    componentDidMount() {
        axios.get("/me", {headers: {Authorization: `Bearer ${getToken()}`}}).then(response => {
            console.log(response);
            this.setState({user: response.data});
        })
    }

    render() {
        const {error, isLoaded, user} = this.state;

        if (error) {
            return <Alert color="success">Error: {error.message}</Alert>;
        } else if (!isLoaded) {
            return <div className="loader"/>;
        } else {
            return (
                <>
                    <Navbar className="navbar-top navbar-dark" expand="md" id="navbar-main">
                        <Container fluid>
                            <Link
                                className="h4 mb-0 text-white text-uppercase d-none d-lg-inline-block"
                                to="/"
                            >
                                {this.props.brandText}
                            </Link>
                            <Form
                                className="navbar-search navbar-search-dark form-inline mr-3 d-none d-md-flex ml-lg-auto">
                                <FormGroup className="mb-0">
                                    <InputGroup className="input-group-alternative">
                                        <InputGroupAddon addonType="prepend">
                                            <InputGroupText>
                                                <i className="fas fa-search"/>
                                            </InputGroupText>
                                        </InputGroupAddon>
                                        <Input placeholder="Search" type="text"/>
                                    </InputGroup>
                                </FormGroup>
                            </Form>
                            <Nav className="align-items-center d-none d-md-flex" navbar>
                                <UncontrolledDropdown nav>
                                    <DropdownToggle className="pr-0" nav>
                                        <Media className="ml-2 d-none d-lg-block">
                      <span className="mb-0 text-sm font-weight-bold">
                        {this.state.user['username']}
                      </span>
                                        </Media>
                                        {/*</Media>*/}
                                    </DropdownToggle>
                                    <DropdownMenu className="dropdown-menu-arrow" right>
                                        <DropdownItem className="noti-title" header tag="div">
                                            <h6 className="text-overflow m-0">Welcome!</h6>
                                        </DropdownItem>
                                        <DropdownItem to="/admin/user-profile" tag={Link}>
                                            <i className="ni ni-single-02"/>
                                            <span>My profile</span>
                                        </DropdownItem>
                                        <DropdownItem divider/>
                                        <DropdownItem href="#pablo" onClick={deleteTokens}>
                                            <i className="ni ni-user-run"/>
                                            <span>Logout</span>
                                        </DropdownItem>
                                    </DropdownMenu>
                                </UncontrolledDropdown>
                            </Nav>
                        </Container>
                    </Navbar>
                </>
            );
        }
    }
}

export default AdminNavbar;
