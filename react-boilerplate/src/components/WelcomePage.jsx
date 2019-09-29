import React, {PureComponent} from 'react';
import Number from './Chart';
import Average from './Average';

class WelcomePage extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    return (
      <div>
        <h1 className='title'>YouCompress</h1>
        <h2>Number of Individuals in Frame (minutes)</h2>
        <div>
          <Number></Number>
        </div>
        <h2>Average Time Spent in Frame (seconds)</h2>
        <div>
          <Average></Average>
        </div>
      </div>
    );
  }
}

export default WelcomePage;
