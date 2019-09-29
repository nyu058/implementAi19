import React, { PureComponent } from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';

const data = [
  {
    name: '0', seconds: 40
  },
  {
    name: '10', seconds: 30
  },
  {
    name: '20', seconds: 34
  },
  {
    name: '30', seconds: 10
  },
  {
    name: '40', seconds: 22
  },
  {
    name: '50', seconds: 70
  },
  {
    name: '60', seconds: 23
  },
  {
    name: '70', seconds: 15
  },
  {
    name: '80', seconds: 8
  },
  {
    name: '90', seconds: 5
  }
];

export default class Average extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/xqjtetw0/';

  render() {
    return (
      <LineChart
        width={1000}
        height={300}
        data={data}
        margin={{
          top: 0, right: 0, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="seconds" stroke="#8884d8" activeDot={{ r: 8 }} />
      </LineChart>
    );
  }
}
