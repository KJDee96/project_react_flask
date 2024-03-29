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

// reactstrap components
import {
    Badge,
    Card,
    CardHeader,
    CardFooter,
    DropdownMenu,
    DropdownItem,
    UncontrolledDropdown,
    DropdownToggle,
    Media,
    Pagination,
    PaginationItem,
    PaginationLink,
    Progress,
    Table,
    Container,
    Row,
    UncontrolledTooltip
} from "reactstrap";
// core components
import Header from "components/Headers/Header.js";
import axios from "axios";
import {getToken, isLoggedIn} from "../../authHelpers";
import {Link, Redirect} from "react-router-dom";

class Tables extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            id: (new URLSearchParams(window.location.search)).get("job"),
            type: (new URLSearchParams(window.location.search)).get("type"),
            job: '',
            jobs: []
        }
    }

    getData() {
        this.setState({id: (new URLSearchParams(window.location.search)).get("job")})

        axios.get("/jobs/" + this.state.id, {headers: {Authorization: `Bearer ${getToken()}`}}).then(response => {
            this.setState({job: response.data});
        })

        axios.get("/jobs/matching/" + this.state.type + "/" + this.state.id, {headers: {Authorization: `Bearer ${getToken()}`}}).then(response => {
            this.setState({jobs: response.data});
        })
    }

    componentDidMount() {
        this.getData()
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (prevProps.location.key !== this.props.location.key) {
            window.location.reload()
        }
    }

    render() {
        const {jobs = []} = this.state;
        return (
            <>
                <Header/>
                {/* Page content */}
                <Container className="mt--7" fluid>
                    <Row>
                        <div className="col">
                            <Card className="shadow">
                                <CardHeader className="border-0">
                                    <h3 className="mb-0">Similar Jobs to {this.state.job['job_title']}</h3>
                                </CardHeader>
                                <Table className="align-items-center table-flush" responsive>
                                    <thead className="thead-light">
                                    <tr>
                                        <th scope="col">Title</th>
                                        <th scope="col">City</th>
                                        <th scope="col">State</th>
                                        <th scope="col">Country</th>
                                        <th scope="col">End Date</th>
                                        <th scope="col"/>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    {jobs.length ?
                                        jobs.map(job => (
                                            <tr>
                                                <td className="ellipsis">{job['job_title']}</td>
                                                <td>{job['city']}</td>
                                                <td>{job['state']}</td>
                                                <td>{job['country']}</td>
                                                <td>{job['end_date']}</td>
                                                <td className="text-right">
                                                    <UncontrolledDropdown>
                                                        <DropdownToggle
                                                            className="btn-icon-only text-light"
                                                            href="#pablo"
                                                            role="button"
                                                            size="sm"
                                                            color=""
                                                            onClick={e => e.preventDefault()}
                                                        >
                                                            <i className="fas fa-ellipsis-v"/>
                                                        </DropdownToggle>
                                                        <DropdownMenu className="dropdown-menu-arrow" right>
                                                            <DropdownItem
                                                                href="#pablo"
                                                                onClick={e => e.preventDefault()}
                                                            >
                                                                View job
                                                            </DropdownItem>
                                                            <DropdownItem
                                                                href="#pablo"
                                                                onClick={e => e.preventDefault()}
                                                            >
                                                                <Link
                                                                    to={"/admin/matching_jobs/?job=" + job['id'] + '&type=cosine'}>DEBUG
                                                                    - View
                                                                    similar jobs - Metric 1</Link>
                                                            </DropdownItem>
                                                            <DropdownItem
                                                                href="#pablo"
                                                                onClick={e => e.preventDefault()}
                                                            >
                                                                <Link
                                                                    to={"/admin/matching_jobs/?job=" + job['id'] + '&type=euclidean'}>DEBUG
                                                                    - View
                                                                    similar jobs - Metric 2</Link>
                                                            </DropdownItem>

                                                        </DropdownMenu>
                                                    </UncontrolledDropdown>
                                                </td>
                                            </tr>
                                        ))
                                        :
                                        (<tr>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                        </tr>)
                                    }
                                    </tbody>
                                </Table>
                            </Card>
                        </div>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Tables;
