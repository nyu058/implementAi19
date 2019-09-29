import React from 'react';
import renderer from 'react-test-renderer';
import {mount, shallow} from 'enzyme';
import WelcomePage from '../../src/components/WelcomePage';
import Logo from '../assets/images/react.png';

describe('WelcomePage', () => {
  it('should match the existing snapshot', () => {
    const realDate = Date;
    const mockDate = new Date(1542531108880);
    mockDate.toLocaleDateString = () => mockDate.toISOString().substring(0, 10);
    mockDate.toLocaleTimeString = () => mockDate.toISOString().substring(11, 19);
    Date = jest.fn(() => mockDate);

    const snapshot = renderer.create(<WelcomePage/>).toJSON();
    expect(snapshot).toMatchSnapshot();

    Date = realDate;
  });

  it('should match the time and date shown', () => {
    const wrapper = shallow(<WelcomePage/>);

    expect(wrapper.state().date.toLocaleTimeString()).toEqual((new Date()).toLocaleTimeString());
    expect(wrapper.state().date.toLocaleDateString()).toEqual((new Date()).toLocaleDateString());
  });

  it('should match the time and date shown', () => {
    var wrapper = mount(<WelcomePage/>);
    const time = wrapper.find('div.time').find('span.subtitle');

    time.props().onClick();
    expect(wrapper.state().displayTime).toEqual(false);
    expect(time.text()).toEqual((new Date()).toLocaleDateString());
  });
});
