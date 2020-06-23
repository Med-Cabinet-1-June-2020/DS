from flask import Flask, render_template, jsonify, Blueprint
from web_app.services.model_service import modelservice

# from web_app.services import _____

med_routes = Blueprint("med_routes", __name__)

@med_routes.route("/dummy_data", methods=['GET'])
def dummy_data(): 
    return jsonify([
    {"strain":"Afpak",
    "race":"hybrid",
    "flavors":["Earthy","Chemical","Pine"],
    "positive":["Relaxed","Hungry","Happy","Sleepy"],
    "negative":["Dizzy"],
    "medical":["Depression","Insomnia","Pain","Stress","Lack of Appetite"],
    "Type":"hybrid",
    "Rating":4.2,
    "Description":"Afpak, named for its direct Afghani and Pakistani landrace heritage, is a beautiful indica-dominant hybrid with light green and deep bluish purple leaves. The taste and aroma are floral with a touch of lemon, making the inhale light and smooth. Its effects start in the stomach by activating the appetite. There is also a potent relaxation that starts in the head and face, and gradually sinks down into the body. Enjoy this strain if you\\u2019re suffering from stress, mild physical discomfort, or having difficulty eating. \\u00a0"},
    
    {"strain":"African",
    "race":"sativa",
    "flavors":["Spicy\\/Herbal","Pungent","Earthy"],
    "positive":["Euphoric","Happy","Creative","Energetic","Talkative"],
    "negative":["Dry Mouth"],
    "medical":["Depression","Pain","Stress","Lack of Appetite","Nausea","Headache"],
    "Type":"sativa",
    "Rating":3.9,
    "Description":"African refers to\\u00a0the indigenous varieties of cannabis (or\\u00a0landraces) that grow natively in this region of the world. Because of this region\'s latitude and climate, these native landrace strains tend to be\\u00a0sativa\\u00a0in structure and effect."},
    
    {"strain":"Afternoon Delight",
    "race":"hybrid",
    "flavors":["Pepper","Flowery","Pine"],
    "positive":["Relaxed","Hungry","Euphoric","Uplifted","Tingly"],
    "negative":["Dizzy","Dry Mouth","Paranoid"],
    "medical":["Depression","Insomnia","Pain","Stress","Cramps","Headache"],
    "Type":"hybrid",
    "Rating":4.8,
    "Description":"Afternoon Delight, created by Colorado Seed Inc.,\\u00a0is a difficult strain to track down. Noted for its small, dense nuggets and an aroma of pine and pungent terpenes, Afternoon Delight is described as an indica-dominant hybrid with a hazy aura that engulfs the mind and body. But indulge with caution, as this hybrid has also been known for its potency.\\u00a0"},
    
    {"strain":"Afwreck",
    "race":"hybrid",
    "flavors":["Pine","Earthy","Flowery"],
    "positive":["Relaxed","Happy","Creative","Uplifted","Sleepy"],
    "negative":["Dizzy","Dry Mouth","Paranoid","Dry Eyes"],
    "medical":["Pain","Stress","Headache","Fatigue","Headaches","Muscle Spasms"],
    "Type":"hybrid",
    "Rating":4.2,
    "Description":"Afwreck is a hybrid cross of Afghani and Trainwreck. \\u00a0Strong sativa effects with immediate head-concentrated high."},
    
    {"strain":"Agent Orange",
    "race":"hybrid",
    "flavors":["Citrus","Orange","Sweet"],
    "positive":["Relaxed","Euphoric","Happy","Energetic","Uplifted"],
    "negative":["Dizzy","Dry Mouth","Paranoid","Dry Eyes"],
    "medical":["Depression","Pain","Stress","Nausea","Headache","Headaches"],
    "Type":"hybrid",
    "Rating":4.2,
    "Description":"Don\\u2019t let the name scare you! The only herbicidal warfare Agent Orange will wage is between the excellence of this strain\'s flavors and uplifting effects. A well-balanced hybrid that combines the smooth Orange Velvet with the bold Jack the Ripper, Agent Orange will capture your senses. Wonderful smells of oranges and fresh-cut citrus fruit will entice you immediately, while the pigments of deep maroon and purple will make this bud stand out in a sea of green. The effects are uplifting and motivating, serving as a great mood enhancer if you are feeling lethargic or depressed."},
    
    {"strain":"Agent Tangie",
    "race":"hybrid",
    "flavors":["Skunk","Pepper","Citrus"],
    "positive":["Euphoric","Happy","Creative","Uplifted","Focused"],
    "negative":["Dry Mouth","Dry Eyes"],
    "medical":["Depression","Stress","Cramps","Fatigue","Eye Pressure"],
    "Type":"hybrid",
    "Rating":4.5,
    "Description":"For those craving a cerebral buzz with a citrus kick, 3C Agent Tangie is perfect. The glittery colas are light green with a zesty, floral flavor. Its effects linger in the crown of the skull and disperse throughout the body in steady waves of invigoration. This strain may assist those suffering from perpetual procrastination, depression, and fatigue.\\u00a0"},
    
    {"strain":"Alaska",
    "race":"sativa",
    "flavors":["Earthy","Woody","Pungent"],
    "positive":["Relaxed","Euphoric","Happy","Energetic","Focused"],
    "negative":["Dizzy","Paranoid","Dry Eyes","Anxious"],
    "medical":["Depression","Pain","Stress","Lack of Appetite","Headaches"],
    "Type":"sativa",
    "Rating":4.6,
    "Description":"Alaska, developed by Tikun Olam, is an Israeli strain comprised of 70%\\u00a0sativa genetics. With uplifting effects intended for daytime consumption, Alaska has been found to successfully treat an array of medical symptoms including inflammation, pain, nausea, insomnia, and gastrointestinal disorders.\\u00a0"},
    
    {"strain":"Alaska Thunder Grape",
    "race":"hybrid",
    "flavors":["Grape","Pepper","Skunk"],
    "positive":["Relaxed","Euphoric","Creative","Tingly","Focused"],
    "negative":[],
    "medical":["Pain","Stress","Eye Pressure"],
    "Type":"hybrid",
    "Rating":5.0,
    "Description":"From Sonoma County comes Alaska Thunder Grape, a hybrid strain that balances genetics from Matanuska Thunder Fuck and Grape Ape. With floral flavors of lavender and hibiscus, Alaska Thunder Grape delivers heavy euphoric effects that promote rest and relaxation."},
    
    {"strain":"Alaskan Ice",
    "race":"sativa",
    "flavors":["Earthy","Pine","Minty"],
    "positive":["Euphoric","Happy","Creative","Energetic","Uplifted"],
    "negative":["Dizzy","Dry Mouth","Paranoid","Dry Eyes"],
    "medical":["Depression","Pain","Stress","Fatigue","Headaches"],
    "Type":"sativa",
    "Rating":4.4,
    "Description":"Alaskan Ice by Green House Seeds is a powerful sativa that crosses a euphoric White Widow hybrid with the energizing buzz of Haze. Frostlike resin blankets the buds in a promise of soaring psychoactivity, anchored only by its moderate CBD content. The intensity of this 70% sativa strain is recommended for evening consumption and unproductive weekends. Alaskan Ice is a slight variant of Moby Dick, but poses a greater challenge to growers; cultivators with the expertise to raise Alaskan Ice will be rewarded with a highly potent harvest of sour, spicy buds following a 9 week flowering period. The high resin content of Alaskan Ice has made this strain a favorite among hash producers and patients with severe symptoms."},
    
    {"strain":"Alaskan Thunder Fuck",
    "race":"sativa",
    "flavors":["Earthy","Woody","Pine"],
    "positive":["Relaxed","Euphoric","Happy","Energetic","Uplifted"],
    "negative":["Dizzy","Dry Mouth","Paranoid","Dry Eyes"],
    "medical":["Depression","Pain","Stress","Lack of Appetite","Headache","Fatigue"],
    "Type":"sativa",
    "Rating":4.4,
    "Description":"Alaskan Thunder Fuck (also referred to as ATF, Matanuska Thunder Fuck or Matanuska Tundra) is a legendary sativa-dominant strain originating in the Matanuska Valley area of Alaska. \\u00a0According to the legend, it was originally a Northern California sativa crossed with a Russian ruderalis, but sometime in the late 70s it was crossed with Afghani genetics to make it heartier. \\u00a0ATF usually presents large, beautifully frosted buds with incredibly strong odors of pine, lemon, menthol, and skunk. \\u00a0Known for possessing a relaxing yet intensely euphoric high, it is also described as having a \\u201ccreeper\\u201d effect as well as pronounced appetite enhancement."}
    
])
