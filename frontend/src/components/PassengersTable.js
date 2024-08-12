import React, { useEffect, useState } from "react";
import DataTable from "react-data-table-component";
import { fetchPassengers } from "../api/passengerApi";

const PassengersTable = () => {
  const [passengers, setPassengers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchPassengers();
        setPassengers(data);
      } catch (err) {
        setError("Failed to fetch passengers.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  const columns = [
    { name: "PassengerId", selector: (row) => row.PassengerId, sortable: true },
    { name: "Survived", selector: (row) => row.Survived, sortable: true },
    { name: "Pclass", selector: (row) => row.Pclass, sortable: true },
    {
      name: "Name",
      selector: (row) => row.Name,
      sortable: true,
      searchable: true,
    },
    { name: "Sex", selector: (row) => row.Sex, sortable: true },
    { name: "Age", selector: (row) => row.Age, sortable: true },
    { name: "SibSp", selector: (row) => row.SibSp, sortable: true },
    { name: "Parch", selector: (row) => row.Parch, sortable: true },
    { name: "Ticket", selector: (row) => row.Ticket, sortable: true },
    { name: "Fare", selector: (row) => row.Fare, sortable: true },
    { name: "Cabin", selector: (row) => row.Cabin, sortable: true },
    { name: "Embarked", selector: (row) => row.Embarked, sortable: true },
  ];

  return (
    <div className="container">
      <h1>Passenger List</h1>
      <DataTable
        columns={columns}
        data={passengers}
        pagination
        fixedHeader
        highlightOnHover
        responsive
      />
    </div>
  );
};

export default PassengersTable;
