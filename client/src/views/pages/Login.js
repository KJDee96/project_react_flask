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
import axios from 'axios';
import {isLoggedIn, isLoggedInRedirect} from "authHelpers"

// reactstrap components
import {
    Button,
    Card,
    CardHeader,
    CardBody,
    FormGroup,
    Form,
    Input,
    InputGroupAddon,
    InputGroupText,
    InputGroup,
    Row,
    Col,
    NavLink
} from "reactstrap";

class Login extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: "",
            password: ""
        }
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
    }

    handleUsernameChange(event) {
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event) {
        this.setState({password: event.target.value});
    }

    handleSignIn = e => {
        e.preventDefault();
        axios.post("/login", this.state).then(response => {
            console.log(response);
            localStorage.setItem('access_token', response.data["access_token"]);

            localStorage.setItem('username', response.data["username"]);

            if (isLoggedIn()) {
                this.props.history.push('/admin/index');
            } else {
                alert(response["error"]);
            }

        }).catch(error => {
            console.log("ERROR: ", error);
        });
    }

    render() {
        return (
            <>
                {isLoggedInRedirect()}
                <Col lg="5" md="7">
                    <Card className="bg-secondary shadow border-0">
                        <CardHeader className="bg-transparent pb-5">
                            <div className="text-muted text-center mt-2 mb-3">
                                <small>Sign in with</small>
                            </div>
                            <div className="btn-wrapper text-center">
                                <Button
                                    className="btn-neutral btn-icon"
                                    color="default"
                                    href="#pablo"
                                    onClick={e => e.preventDefault()}
                                >
                  <span className="btn-inner--icon">
                    <img
                        alt="..."
                        src={require("assets/img/icons/common/github.svg")}
                    />
                  </span>
                                    <span className="btn-inner--text">Github</span>
                                </Button>
                                <Button
                                    className="btn-neutral btn-icon"
                                    color="default"
                                    href="#pablo"
                                    onClick={e => e.preventDefault()}
                                >
                  <span className="btn-inner--icon">
                    <img
                        alt="..."
                        src={require("assets/img/icons/common/google.svg")}
                    />
                  </span>
                                    <span className="btn-inner--text">Google</span>
                                </Button>
                            </div>
                        </CardHeader>
                        <CardBody className="px-lg-5 py-lg-5">
                            <div className="text-center text-muted mb-4">
                                <small>Or sign in with credentials</small>
                            </div>
                            <Form role="form" onSubmit={this.handleSignIn}>
                                <FormGroup className="mb-3">
                                    <InputGroup className="input-group-alternative">
                                        <InputGroupAddon addonType="prepend">
                                            <InputGroupText>
                                                <i className="ni ni-circle-08"/>
                                            </InputGroupText>
                                        </InputGroupAddon>
                                        <Input
                                            placeholder="Username"
                                            type="text"
                                            autoComplete="new-username"
                                            value={this.state.username}
                                            onChange={this.handleUsernameChange}/>
                                    </InputGroup>
                                </FormGroup>
                                <FormGroup>
                                    <InputGroup className="input-group-alternative">
                                        <InputGroupAddon addonType="prepend">
                                            <InputGroupText>
                                                <i className="ni ni-lock-circle-open"/>
                                            </InputGroupText>
                                        </InputGroupAddon>
                                        <Input placeholder="Password"
                                               type="password"
                                               autoComplete="new-password"
                                               value={this.state.password}
                                               onChange={this.handlePasswordChange}
                                        />

                                    </InputGroup>
                                </FormGroup>
                                <div className="custom-control custom-control-alternative custom-checkbox">
                                    <input
                                        className="custom-control-input"
                                        id=" customCheckLogin"
                                        type="checkbox"
                                    />
                                    <label
                                        className="custom-control-label"
                                        htmlFor=" customCheckLogin"
                                    >
                                        <span className="text-muted">Remember me</span>
                                    </label>
                                </div>
                                <div className="text-center">
                                    <Button className="my-4" color="primary" type="submit">
                                        Sign in
                                    </Button>
                                </div>
                            </Form>
                        </CardBody>
                    </Card>
                    <Row className="mt-3">
                        <Col xs="6">
                            <a
                                className="text-light"
                                onClick={e => e.preventDefault()}
                            >
                                <small>Forgot password?</small>
                            </a>
                        </Col>
                        <Col className="text-right text-light" xs="6"
                             to="/auth/register"
                             tag={Link}
                        >
                            <small>Create new account</small>

                        </Col>
                    </Row>
                </Col>
            </>
        );
    }
}

export default Login;
