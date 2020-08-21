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
import Index from "views/Index.js";
import Profile from "views/pages/Profile.js";
import Register from "views/pages/Register.js";
import Login from "views/pages/Login.js";
import Tables from "views/pages/Tables.js";
import Icons from "views/pages/Icons.js";
import Jobs from "views/pages/Jobs.js";
import SimilarJobs from "views/pages/SimilarJobs.js"
import Applications from "views/pages/Applications.js"
import RecommendedJobs from "views/pages/RecommendedJobs.js"

var routes = [
  {
    path: "/index",
    name: "Admin Dashboard Example",
    icon: "ni ni-tv-2 text-primary",
    component: Index,
    layout: "/admin",
    visible: true
  },
  {
    path: "/icons",
    name: "Icons",
    icon: "ni ni-planet text-blue",
    component: Icons,
    layout: "/admin",
    visible: false
  },
  // {
  //   path: "/user-profile",
  //   name: "User Profile",
  //   icon: "ni ni-single-02 text-yellow",
  //   component: Profile,
  //   layout: "/admin",
  //   visible: true
  // },
  {
    path: "/tables",
    name: "Tables",
    icon: "ni ni-bullet-list-67 text-red",
    component: Tables,
    layout: "/admin",
    visible: false
  },
  {
    path: "/jobs",
    name: "All Jobs",
    icon: "ni ni-briefcase-24 text-green",
    component: Jobs,
    layout: "/admin",
    visible: true
  },
  {
    path: "/matching_jobs",
    name: "Similar Jobs",
    icon: "ni ni-briefcase-24 text-green",
    component: SimilarJobs,
    layout: "/admin",
    visible: false
  },
  {
    path: "/recommended_jobs",
    name: "Recommended Jobs",
    icon: "ni ni-briefcase-24 text-green",
    component: RecommendedJobs,
    layout: "/admin",
    visible: true
  },
  {
    path: "/applications",
    name: "My Applications",
    icon: "ni ni-briefcase-24 text-green",
    component: Applications,
    layout: "/admin",
    visible: true
  },
  {
    path: "/login",
    name: "Login",
    icon: "ni ni-key-25 text-info",
    component: Login,
    layout: "/auth",
    visible: false
  },
  {
    path: "/register",
    name: "Register",
    icon: "ni ni-circle-08 text-pink",
    component: Register,
    layout: "/auth",
    visible: false
  }
];
export default routes;
