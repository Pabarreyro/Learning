import React from 'react';

class NewTicketControl extends React.Component {

  constructor(props) {
    super(props);
    this.state = {formVisiblePage: false};
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(){
    this.setState({formVisiblePage: true});
    console.log('formVisibleOnPage is currently set to:' + this.state.formVisibleOnPage);
  }

  render() {
    return (
      <div>
        <p>This is the NewTicketControl component!</p>
        <strong onClick={this.handleClick}>Click me to change my state!</strong>
      </div>
    );
  }
}

export default NewTicketControl;
