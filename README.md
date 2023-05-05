# Song-Popularity-Predictor
Song popularity predictor is an ml tool that is used to predict the popularity of the newly released songs on the basis of their audio features


Song Popularity predictor is trained on a large dataset that contains song and audio features, extracted using **Spotipy a Spotify API**.<br/>
This is the landing page:
![image](https://user-images.githubusercontent.com/90406492/236518205-49aae9f5-b349-4c92-a69e-35ead0f543c8.png)

-> The background and theme is created using HTML, CSS and Javascript<br/>
-> **Particles.js** and **Typed.js** is used to provide a very beautiful background and title<br/>
<br/>

Song url should be copied as such:
![image](https://user-images.githubusercontent.com/90406492/236519157-bf94abc2-f9ca-4f19-bb7e-647875c46a10.png)

Spotify link of the track or album is provided in the input here:
![image](https://user-images.githubusercontent.com/90406492/236519219-7358e47a-75a1-4d03-8f2f-d9a06283ff5a.png)

The popularity of the chosen song is shown as below:
![image](https://user-images.githubusercontent.com/90406492/236520604-c8b986b5-a487-42eb-9e49-cc9e9d22d028.png)

<br/>
-> The Application uses <strong>Flask</strong> and <strong>Pickle</strong> to integrate the model with the frontend<br/>
-> <strong>DecisionTreeRegressor</strong> is used as the model to solve regression problems and provides high accuracy<br/>
-> <strong>Spotify API (Spotipy)</strong> is used to extract features of the audio uploaded in spotify platform<br/>
