import React from "react";

export default function Login() {
    return (
        <form>
            <div className="mb-3 row">
                <label for="staticEmail" className="col-sm-2 col-form-label">Email</label>
                <div className="col-sm-5">
                    <input type="text" className="form-control" id="staticEmail" />
                </div>
            </div>
            <div className="mb-3 row">
                <label for="inputPassword" className="col-sm-2 col-form-label">Password</label>
                <div className="col-sm-5">
                    <input type="password" className="form-control" id="inputPassword" />
                </div>
            </div>
            <div class="col-auto">
                <button type="submit" class="btn btn-primary mb-3">Confirm identity</button>
            </div>
        </form>
    )
}