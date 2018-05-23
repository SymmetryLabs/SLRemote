from flask import Flask, render_template, request, redirect, url_for
from forms import RemoteForm, TestForm, RegistrationForm, UndercardForm
from utils_light import *
from flask_babel import Babel
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
babel = Babel()
# bootstrap = Bootstrap(app)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def remote():
    form = RemoteForm()
    print('inside quick add routes')
    if form.validate_on_submit(): 
        print('form test msg:')

        print(form.brightness.data)
        change_pattern(form.pattern.data)
        change_brightness(float(form.brightness.data))
        change_color(float(form.color.data))
        change_speed(float(form.speed.data))
        turn_on(form.on_off.data)
     
        if form.clip1.data:
            print('clip1')
            return redirect(url_for('remote'))
        if form.clip2.data:
            print('clip2')
            return redirect(url_for('remote'))
        if form.clip3.data:
            print('clip3')
            return redirect(url_for('remote'))
        if form.submit.data:
            print(('submit'))
            return redirect(url_for('remote'))

    return render_template('remote.html', form=form)

@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm(csrf_enabled=False)
    print(form.age.data)

    if form.validate():
        


        print(request.form["name_of_slider"])
        print('form test msg:')
        print(form.age.data)
        
        #print(request.form["outputtest"])
        return redirect(url_for('main.test'))

    return render_template('test.html', form=form)

@app.route('/undrcrd', methods=['GET', 'POST'])
def undrcrd():
    form = UndercardForm()
    scope = 'user-top-read user-read-playback-state user-read-recently-played'
    print('at spotify')
    if form.validate_on_submit():
        print('spotify form went thru')
        
        #scope = 'user-read-playback-state user-read-recently-played'
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='9741d373ad3d479fb8dc135f53580e71', redirect_uri='http://localhost:5555/redirect',  scope=scope)
        print('sp oauth:' , sp_oauth)
        auth_url = sp_oauth.get_authorize_url()
        
        webbrowser.open(auth_url)
        token = block_until_token(sp_oauth)
        #print('data', form.spotify_uzsername.data)
        print('token', token)
        # token = util.prompt_for_user_token('kushaan', scope, client_id='dbe2a20785304190b8e35d5d6644397b', client_secret='d73cf4a1525c44e899feeeff4b840040', redirect_uri='http://localhost:3000')
        if token:
            top_artists = []
            sp = spotipy.Spotify(auth=token)
            #print(sp.user())
            username = sp.user(form.spotify_username.data)
            
            sp.trace=False
            #ranges = ['short_term', 'medium_term', 'long_term']
            #print 'token went thru!'
            #for range in ranges:
                #print "range:", range
            artist_results = sp.current_user_top_artists(time_range='short_term', limit=10)
            user_artists_dict = {}

            for i, item in enumerate(artist_results['items']):
                print(i, item['name'])
                top_artists.append(item['name'])
                user_artists_dict[i+1] = item['name']

                # if i > 10:
                #     break
            
            # user_artists = []
            
            # for j, top in enumerate(top_artists):
            #     user_artists.append(top)#.encode('ascii','ignore')) 
                
            # print('top artists type:', type(top_artists))
            # print('user artists type:', type(user_artists))
            print('user atists dift:', user_artists_dict)
            # todo: change user_id to point to current_user or the user table!

            if type(current_user) == str:
                spotify_user = current_user
            else:
                spotify_user = 0
                print('spotify user type', type(spotify_user))
            sp_df = pd.DataFrame.from_dict(user_artists_dict, orient='index')
            sp_df['genre'] = ''
            sp_df['username'] = current_user.username

            
            #entry_1 = [form.media_name_1.data, form.genre_1.data, form.comment_1.data, current_user.username]
            #entry_2 = [form.media_name_2.data, form.genre_2.data, form.comment_2.data, current_user.username]
            #entry_3 = [form.media_name_3.data, form.genre_3.data, form.comment_3.data, current_user.username]
            #add_entry(worksheet, entry_1, empty_row)
            # add to DB - will come back to this.
            user_artists_dict_p = pprint.pformat(user_artists_dict)
            
            artists = Artists(user_id=current_user.username, spotify_id=form.spotify_username.data, #user_id=spotify_user,
                    top_artists=str(user_artists_dict)) #str(user_artists))
            #db.session.add(artists)
            #db.session.commit()
            print(user_artists_dict_p)
            flash(_('your top artists: ' + user_artists_dict_p))


            return redirect(url_for('main.index', username=current_user.username))
            # code to match up w SXSW ! - TODO: get local SF shows ;)
            # with open('/Users/aaronopp/Desktop/GOOD_MEDIA/SXSetFinder/app/artist_list_trimmed_final.csv', 'r') as f:
            #     reader = csv.reader(f)
            #     your_list = list(reader)
            #     artist_list_3_15_f = your_list[0]


            # lowest_matches_dict = get_lowest_artist_matches(user_artists[:3], artist_list_3_15_f)

            # predicted_artists = []
            # for value in lowest_matches_dict:
            #     predicted_artists.append(value['SXSW_artist'])
    
            # predicted_artists = set(list(predicted_artists))
            # print('DONE', predicted_artists)
            # song_results = sp.current_user_top_tracks(time_range='short_term', limit=50)
            # print(type(artist_results))
            # for i, item in enumerate(song_results['items']):
            #     print(i, item['name'])
            # print()
        else:
            print('cant get token for', form.spotify_username.data)

    #else:
        #print 'spotify form didnt go thru'
    return render_template('undrcrd.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
