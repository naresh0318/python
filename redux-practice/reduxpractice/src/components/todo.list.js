/* eslint-disable no-unused-vars */
import React, { useEffect } from "react";
import TodoItem from "./todo.item";
import { useSelector, useDispatch } from "react-redux";
import { clearTodoList } from "../redux/actions/index";

const TodoList = () => {
  const { list } = useSelector(state => state.todos);
  const dispatch = useDispatch();

  const handleClearList = () => {
    dispatch(clearTodoList());
  };

  return (
    <div>
      <ul className="list-group my-5 border border-light">
        <h3 className="text-capitalize text-center">TRANSECTION's HISTORY</h3>
        {list.map(todo => (
          <TodoItem key={todo.id} {...todo} />
        ))}
      </ul>
      <button
        type="button"
        className="btn btn-danger btn-block text-capitalize mt-5"
        onClick={handleClearList}
      >
        Delete transection
      </button>
    </div>
  );
};

export default TodoList;