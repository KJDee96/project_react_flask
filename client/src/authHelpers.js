import React from "react";
import Redirect from "react-router-dom/es/Redirect";

export function isLoggedIn() {
    return localStorage.getItem("access_token") !== null && localStorage.getItem("access_token") !== "undefined";
}


export function isLoggedInRedirect() {
    if (isLoggedIn()) {
        return (<Redirect to='/admin/index'/>);
    }
}

export function getToken() {
    return localStorage.getItem("access_token");
}


export function deleteTokens() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("username");
}

export function requiredAuth() {
    if (!isLoggedIn()) {
        return (<Redirect to='/auth/login'/>);
    }
}

export function logout() {
    deleteTokens();
    isLoggedInRedirect();
}