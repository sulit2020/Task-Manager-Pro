import { useMutation, gql } from "@apollo/client";
import { useState } from "react";
import { GET_TASKS } from "./Tasks";

const CREATE_TASK = gql`
  mutation($title: String!) {
    createTask(title: $title) {
      task {
        id
        title
        completed
      }
    }
  }
`;


const TaskForm = () => {
  const [title, setTitle] = useState("");
  const [createTask] = useMutation(CREATE_TASK, {
    refetchQueries: [{ query: GET_TASKS }],
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title) return;
    createTask({ variables: { title } });
    setTitle("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="New Task"
      />
      <button type="submit">Add</button>
    </form>
  );
}

export default TaskForm
