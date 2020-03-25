import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      acousticness: 0,
      danceability: 0, 
      duration_ms: 0, 
      energy: 0, 
      instrumentalness: 0,
      key: 0, 
      liveness: 0, 
      loudness: 0, 
      mode: 0, 
      speechiness: 0,
      tempo: 0, 
      time_signature: 0, 
      valence: 0,
      popularity:0,
      resultsShown: false
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.tryAgain = this.tryAgain.bind(this);
    }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log('submit');
    const myForm = document.getElementById('formElem');

    const myRequest = new Request('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: new FormData(myForm)
    });

    fetch(myRequest)
      .then(res => res.json())
      .then(res => { 
        console.log(res.popularity_bin);
        this.setState({
          popularity: res.popularity_bin,
          resultsShown: true
        });

      });
  }

  tryAgain(){
    this.setState({
      resultsShown: false
    });
  }

  render() {
    const resultsShown = this.state.resultsShown;
    const popularity = this.state.popularity;
    return (
      <div className = "App" >
        <header className="App-header">Determining Song Success!</header><br></br>
        <p>Least popular - 3 {'   '} Medium popularity - 2 {'   '}  Most popular - 0</p>
        <br></br>
        {resultsShown ? 
        <div>
          <header className="App-header">The popularity bucket of the song is: {popularity}</header>
          <button onClick={this.tryAgain}> Try Again! </button>
        </div>
        :
        <div>
          <header className = "App-subheader">Input the following features of your song:</header>
          <br></br> 
          <form id = "formElem" onSubmit={this.handleSubmit}>
            <label className="App-label">
              Acousticness:
              <input
                name="acousticness"
                type="number"
                value={this.state.acousticness}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Danceability:
              <input
                name="danceability"
                type="number"
                value={this.state.danceability}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Duration:
              <input
                name="duration_ms"
                type="number"
                value={this.state.duration_ms}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Energy:
              <input
                name="energy"
                type="number"
                value={this.state.energy}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Instrumentalness:
              <input
                name="instrumentalness"
                type="number"
                value={this.state.instrumentalness}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Key:
              <input
                name="key"
                type="number"
                value={this.state.key}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Liveness:
              <input
                name="liveness"
                type="number"
                value={this.state.liveness}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Loudness:
              <input
                name="loudness"
                type="number"
                value={this.state.loudness}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Mode:
              <input
                name="mode"
                type="number"
                value={this.state.mode}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Speechiness:
              <input
                name="speechiness"
                type="number"
                value={this.state.speechiness}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Tempo:
              <input
                name="tempo"
                type="number"
                value={this.state.tempo}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Time Signature:
              <input
                name="time_signature"
                type="number"
                value={this.state.time_signature}
                onChange={this.handleInputChange} />
            </label>
            <br/>
            <label className="App-label">
              Valence:
              <input
                name="valence"
                type="number"
                value={this.state.valence}
                onChange={this.handleInputChange} />
            </label>
            <input type="submit" value="Submit" />
          </form> 
        </div>
      }
      </div>
    );
  }
}

export default App;
