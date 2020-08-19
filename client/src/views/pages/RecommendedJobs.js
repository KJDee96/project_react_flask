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
import {Link} from "react-router-dom";
import ReactPaginate from 'react-paginate'; // https://medium.com/how-to-react/create-pagination-in-reactjs-e4326c1b9855

class Tables extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            jobs: []
        }
    }

    componentDidMount() {
        this.getData()
    }

    getData(){
        axios.get("/users/my_applications/matching/cosine/", {headers: {Authorization: `Bearer ${getToken()}`}}).then(response => {
            this.setState({jobs: response.data});
            // if (this.state.totalPages === null) {
            //     this.setState({totalPages: response.data['total']})
            // }
        })

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
                                    <h3 className="mb-0">Your Recommended Jobs</h3>
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
                                                                    to={"/admin/matching_jobs/?job=" + job['id'] + '&type=cosine'}>View
                                                                    similar jobs - COSINE</Link>
                                                            </DropdownItem>
                                                            <DropdownItem
                                                                href="#pablo"
                                                                onClick={e => e.preventDefault()}
                                                            >
                                                                <Link
                                                                    to={"/admin/matching_jobs/?job=" + job['id'] + '&type=euclidean'}>View
                                                                    similar jobs - EUCLIDEAN</Link>
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
                                    {/*<tr>*/}
                                    {/*    <th scope="row">*/}
                                    {/*    </th>*/}
                                    {/*    <td>*/}
                                    {/*    </td>*/}
                                    {/*    <td>*/}
                                    {/*    </td>*/}
                                    {/*    <td>*/}
                                    {/*    </td>*/}
                                    {/*    <td>*/}
                                    {/*    </td>*/}
                                    {/*    <td className="text-right">*/}
                                    {/*        <UncontrolledDropdown>*/}
                                    {/*            <DropdownToggle*/}
                                    {/*                className="btn-icon-only text-light"*/}
                                    {/*                href="#pablo"*/}
                                    {/*                role="button"*/}
                                    {/*                size="sm"*/}
                                    {/*                color=""*/}
                                    {/*                onClick={e => e.preventDefault()}*/}
                                    {/*            >*/}
                                    {/*                <i className="fas fa-ellipsis-v"/>*/}
                                    {/*            </DropdownToggle>*/}
                                    {/*            <DropdownMenu className="dropdown-menu-arrow" right>*/}
                                    {/*                <DropdownItem*/}
                                    {/*                    href="#pablo"*/}
                                    {/*                    onClick={e => e.preventDefault()}*/}
                                    {/*                >*/}
                                    {/*                    View job*/}
                                    {/*                </DropdownItem>*/}
                                    {/*                <DropdownItem*/}
                                    {/*                    href="#pablo"*/}
                                    {/*                    onClick={e => e.preventDefault()}*/}
                                    {/*                >*/}
                                    {/*                    View similar jobs*/}
                                    {/*                </DropdownItem>*/}

                                    {/*            </DropdownMenu>*/}
                                    {/*        </UncontrolledDropdown>*/}
                                    {/*    </td>*/}
                                    {/*</tr>*/}
                                    </tbody>
                                </Table>
                                <CardFooter className="py-4">
                                    <nav aria-label="...">
                                        {/*<Pagination*/}
                                        {/*    className="pagination justify-content-end mb-0"*/}
                                        {/*    listClassName="justify-content-end mb-0"*/}
                                        {/*>*/}
                                        {/*    <PaginationItem className="disabled">*/}
                                        {/*        <PaginationLink*/}
                                        {/*            href="#pablo"*/}
                                        {/*            onClick={e => e.preventDefault()}*/}
                                        {/*            tabIndex="-1"*/}
                                        {/*        >*/}
                                        {/*            <i className="fas fa-angle-left"/>*/}
                                        {/*            <span className="sr-only">Previous</span>*/}
                                        {/*        </PaginationLink>*/}
                                        {/*    </PaginationItem>*/}
                                        {/*    <PaginationItem className="active">*/}
                                        {/*        <PaginationLink*/}
                                        {/*            href="#pablo"*/}
                                        {/*            onClick={e => e.preventDefault()}*/}
                                        {/*        >*/}
                                        {/*            1*/}
                                        {/*        </PaginationLink>*/}
                                        {/*    </PaginationItem>*/}
                                        {/*    <PaginationItem>*/}
                                        {/*        <PaginationLink*/}
                                        {/*            href="#pablo"*/}
                                        {/*            onClick={e => e.preventDefault()}*/}
                                        {/*        >*/}
                                        {/*            2 <span className="sr-only">(current)</span>*/}
                                        {/*        </PaginationLink>*/}
                                        {/*    </PaginationItem>*/}
                                        {/*    <PaginationItem>*/}
                                        {/*        <PaginationLink*/}
                                        {/*            href="#pablo"*/}
                                        {/*            onClick={e => e.preventDefault()}*/}
                                        {/*        >*/}
                                        {/*            3*/}
                                        {/*        </PaginationLink>*/}
                                        {/*    </PaginationItem>*/}
                                        {/*    <PaginationItem>*/}
                                        {/*        <PaginationLink*/}
                                        {/*            href="#pablo"*/}
                                        {/*            onClick={e => e.preventDefault()}*/}
                                        {/*        >*/}
                                        {/*            <i className="fas fa-angle-right"/>*/}
                                        {/*            <span className="sr-only">Next</span>*/}
                                        {/*        </PaginationLink>*/}
                                        {/*    </PaginationItem>*/}
                                        {/*</Pagination>*/}
                                    </nav>
                                </CardFooter>
                            </Card>
                        </div>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Tables;
