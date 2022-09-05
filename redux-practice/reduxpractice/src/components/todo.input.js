import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTodo } from "../redux/actions/index";

const TodoInput = () => {
  const [text, setText] = useState("");
  // const todos = useSelector(state => state.todos);

  const dispatch = useDispatch();

  const handleSubmit = event => {
    if (text !== "") {
      dispatch(addTodo(text));
      setText("");
    } else {
    }
    event.preventDefault();
  };

  return (
    <div className="card card-body my-3">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <div className="input-group-prepend">
            
          </div>
          <input
            type="number"
            className="form-control text-capitalize"
            placeholder="amount"
            name="todo"
            value={text}
            onChange={event => setText(event.target.value)}
          />
        </div>
        <button
          className="btn btn-block btn-primary mt-3"
          onClick={handleSubmit}
        >
          transection
        </button>
      </form>
    </div>
  );
};

export default TodoInput;
