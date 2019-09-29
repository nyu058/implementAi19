import React, { PureComponent } from 'react';
import {BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import datafile from './data.json';


let d = datafile['nums_people_in_frame'].map((x, i) => {
    return {name: '' + (i*4) , people: x};
});


export default class Number extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/30763kr7/';

  render() {
    return (
      <BarChart
        width={1000}
        height={300}
        data={d}
        margin={{
          top: 0, right: 0, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="people" fill="#8884d8" />
      </BarChart>
    );
  }
}
