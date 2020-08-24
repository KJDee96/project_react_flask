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
            page: 0,
            totalPages: 50,
            jobs: []
        }
    }

    componentDidMount() {
        this.getData()
    }

    getData() {
        axios.get("/jobs/all?page=" + this.state.page, {headers: {Authorization: `Bearer ${getToken()}`}}).then(response => {
            this.setState({jobs: response.data['jobs']});
        })

    }

    handlePageClick = (e) => {
        const selectedPage = e.selected;

        this.setState({
            page: selectedPage,
        }, () => {
            this.getData()
        });

    };


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
                                    <h3 className="mb-0">Jobs</h3>
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
                                <CardFooter className="py-4">
                                    <nav aria-label="...">
                                        <ReactPaginate
                                            previousLabel={""}
                                            previousClassName={"page-item"}
                                            previousLinkClassName={"page-link fas fa-angle-left"}
                                            nextLabel={""}
                                            nextClassName={"page-item"}
                                            nextLinkClassName={"page-link fas fa-angle-right"}
                                            breakLabel={"..."}
                                            breakClassName={"break-me"}
                                            pageCount={this.state.totalPages}
                                            marginPagesDisplayed={2}
                                            pageRangeDisplayed={5}
                                            onPageChange={this.handlePageClick}
                                            containerClassName={"pagination justify-content-end mb-0"}
                                            subContainerClassName={'pages pagination'}
                                            activeClassName={"active"}
                                            pageClassName={"page-item"}
                                            pageLinkClassName={"page-link"}
                                        />
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
