import React from "react";
import { useDispatch } from "react-redux";
import { bindActionCreators } from "redux";


export default function BalanceControl() {
    const dispatch = useDispatch()    
    return (
        <div className="container">
            <h2>Deposit/Withdraw Money</h2>
            <button className="btn btn-primary mx-2">-</button>  
            Update Balance
            <button className="btn btn-primary mx-2">+</button>  
        </div>
    )
}