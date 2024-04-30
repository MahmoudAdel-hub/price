import streamlit as st
import joblib
import pandas as pd

cols = ['room', 'bath', 'area', 'balcony', 'parking', 'maids_room',
       'pets_allowed', 'gym', 'garden', 'kitchen_appliances', 'heating',
       'elevator', 'natural_gas', 'security', 'water_meter', 'play_area',
       'barbeque_area', 'CCTV', 'maintenance_staff', 'build_in', 'floor',
       'cat__finish_type', 'cat__city', 'cat__district', 'cat__view',
       'cat__kind']


encoder = joblib.load('mahmoud.pkl')
def predict_house_price(room, bath, area, balcony, parking, maids_room,
       pets_allowed, gym, garden, kitchen_appliances, heating,
       elevator, natural_gas, security, water_meter, play_area,
       barbeque_area, CCTV, maintenance_staff, build_in, floor,
       cat__finish_type, cat__city ,cat__district, cat__view ,cat__kind):
    
    features = [[room, bath, area, balcony, parking, maids_room,
       pets_allowed, gym, garden, kitchen_appliances, heating,
       elevator, natural_gas, security, water_meter, play_area,
       barbeque_area, CCTV, maintenance_staff, build_in, floor,
       cat__finish_type, cat__city ,cat__district, cat__view ,cat__kind]]
    
    condition = False
    for _ ,_1 in zip(features[0],cols):
        if _ < 0:
            raise ValueError(f"Enter a Valid Value for : {_1}")
            condition == True
            continue
    if condition == True:
        prediction = "no predictions ,please enter valid values"
        
    else:
        lower = joblib.load('lower.pkl')
        upper = joblib.load('upper.pkl')
        average = joblib.load('average.pkl')
        prediction = f"The lower bound is {lower.predict(features)[0]}, the average estimate is {average.predict(features)[0]}, and the upper bound is {upper.predict(features)[0]}"
    return prediction # Assuming prediction are a multiple values

def main(): 
    st.title("House Price Predictor")
    html_temp = """
    <style>
       .stApp {
        color: white;
    }
    .prediction-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .estimate {
        font-weight: bold;
    }
    .bound {
        margin-top: 5px;
    }
    </style>
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">House Price Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True) 

    room = st.text_input("Bedrooms", "0",help='Enter The Number Of Bedrooms') 
    bath = st.text_input("Bathrooms", "0",help='Enter The Number Of Bathrooms') 
    area = st.text_input("Area", "0",help='Enter The Area') 
    balcony = st.text_input("Balcony", "0",help='The House has Balcony ( 1 ) or not ( 0 )') 
    parking = st.text_input("Parking", "0") 
    maids_room = st.text_input("Maids Room", "0") 
    pets_allowed = st.text_input("Pets Allowed", "0") 
    gym = st.text_input("Gym", "0") 
    garden = st.text_input("Garden", "0") 
    kitchen_appliances = st.text_input("Kitchen Appliances", "0") 
    heating = st.text_input("Heating", "0") 
    elevator = st.text_input("Elevator", "0") 
    natural_gas = st.text_input("Natural Gas", "0") 
    security = st.text_input("Security", "0") 
    water_meter = st.text_input("Water Meter", "0") 
    play_area = st.text_input("Play Area", "0") 
    barbeque_area = st.text_input("Barbeque Area", "0") 
    CCTV = st.text_input("CCTV", "0") 
    maintenance_staff = st.text_input("Maintenance Staff", "0") 
    build_in = st.text_input("Build In", "0") 
    floor = st.text_input("Floor", "0") 
    finish_type = st.selectbox("Finish Type", ['extra_super_lux', 'unfurnished', 'furnished', 'semi_finished',
   'super_lux', 'lux', 'without_finish']) 
    
    city = st.selectbox("City", ['cairo', 'giza', 'matrouh', 'alex', 'suez', 'red_sea'])
    
    district = st.selectbox("District", ['new_cairo', 'shorouk', 'mokattam', 'heliopolis', 'cairo',
   'mostakbal_city', 'nasr_city', 'maadi', 'nozha', 'madinaty',
   'sheikh_zayed', 'hadayek_october', 'north_coast', 'andalous',
   'mandara', 'obour', '5th_settlement', 'ain_sukhna',
   '6th_of_october', 'eastown', 'rehab', '1st_settlement',
   'sidi_bishr', 'ibrahimia', 'katameya', 'agamy', 'village', 'jayd',
   'lake_view', 'gouna', 'nakheel', 'dokki', 'badr_city', 'alamein',
   '9th_settlement', 'hurghada', 'zahraa_el_maadi', 'banafseg_5',
   'zamalek', 'cleopatra', 'sheraton', 'galleria', 'moharam_bik',
   'zaytun', 'mivida', 'narges', 'maryotaya', 'south_investors',
   'saada', 'bolkly', 'zezenia', 'golden_heights', 'san_stefano',
   'gharb_golf', 'les_rois', 'hadayek_el_ahram', 'matarya',
   'creek_town', 'century_city', 'kafr_abdo', 'abo_talat', 'faisal',
   'beit_el_watan', '3rd_settlement', 'ain_shams', 'marsa_matrouh',
   'haram', '4th_settlement', 'gesr_el_suez', 'dyar', 'borg_el_arab',
   'mohandesen', 'seyouf', 'layan', 'manial', 'miami', 'shoubra',
   'laurent', 'lotus', 'helmeya', 'midtown', 'ring_road', 'smouha',
   'mamoura', 'south_of_academy', 'blue_tree', 'camp_caesar',
   'hadara', 'kinda', 'dar_misr', 'saba_basha', 'glim', 'moneeb',
   'mirage', 'asafra', 'address_east', 'amorada', 'raml_station',
   '15th_of_may', 'bellagio', 'sayeda_zeinab', 'stanley', 'montazah',
   'median', 'fleming', 'sidi_gaber', 'shatby', 'grand_residence',
   'roushdy', 'lago_vista', 'amreya', 'yasmeen_2', 'soma_breeze',
   'ataba', 'hadayek_el_koba', 'alex_west', 'abo_qir',
   'north_investors', 'salam_city', 'banafseg_7', 'marg',
   'abo_el_matamer', 'azarita', 'abasiya', 'giza', 'banafseg_2',
   'sahl_hasheesh', 'koronfel', 'boulaq_dakrour', 'sporting',
   'old_cairo', 'ganaklis', 'downtown', 'porto_matrouh', 'zayed',
   '6th_settlement', '2nd_settlement', 'cairo_ismailia_desert_road',
   'beverly_hills', 'uptown', 'soma_bay', 'waha', 'andalus',
   '26th_of_july', 'green_belt', 'dahshur', 'banafseg',
   '17th_settlement', 'hegaz', '12th_settlement',
   'mohamed_naguib_axis', 'safaga', 'sharq', 'agouza', 'abageyah',
   'alex', 'korba', '10th_settlement', '11th_settlement', 'hadaba',
   'almazah', 'el_nadi_el_ahly', '8th_settlement', '13th_settlement',
   'degla', 'narges_6', 'roxy', 'sefarat_district', '7th_settlement',
   'mashal', 'wasat', 'dream_land', 'malek_el_saleh', 'marsa_naqari',
   'banafseg_11', 'red_sea', 'matrouh', 'mariouteya', 'motamayez',
   'rabaa_el_adaweyah', 'king_mariout', 'ain_el_sera', 'banafseg_6',
   'ganoob_el_acadimia', 'sharekat', 'banafseg_9', 'mahkama',
   '16th_settlement', 'fustat', 'mostafa_kamel', 'bulaq_abo_el_ela',
   'bakoos', 'abo_el_houl', 'narges_4', 'narges_7', 'central_axis',
   'garden_city', 'waboor_elmayah', 'zahraa_madinat_nasr',
   'gamea_square', 'hadayek_el_maadi', 'anfoshy', 'sahel', 'tharwat',
   'central_business_district', '14th_settlement', 'banafseg_1',
   'banafseg_8', 'narges_1', 'intercontinental_district', 'estad',
   'saraya', 'gharb', 'attarin', 'ras_el_soda', 'masr_el_kadima',
   'narges_8', 'saft_el-laban', 'fardous_city', 'ganzouri', 'gomrok',
   'ismailia', 'rod_el_farag', 'abdeen', 'banafseg_10', 'tawabek',
   'eshrein', 'abo_sir', 'october', 'sahafeyen', 'hanouvel',
   'other_neighborhoods_in_alexandria', 'lauran', 'victoria',
   'sawary', 'bahray_el_anfoshy', 'new_alexandria',
   'international_coastal_road', 'sidi_kirayr',
   'mehwar_el_tamer_international_coastal_road',
   'cairo_borg_el_arab_desert_road', 'abis', 'karmus',
   'port_of_el_dekheila', 'mahta_el_raml', 'schutz',
   'waboor_el_mayah', 'alexandria_marsa_matrouh_road', 'mansheya',
   'chatby', 'qabari', 'labban', 'ras_el_tin', 'shorouk_city',
   'helwan', 'imbaba', 'na', 'madinat_el_salam', 'zawiya_el_hamra',
   'dar_el_salam', 'other_neighborhoods_in_greater_cairo', 'basaten',
   'bashtil', 'omraneya', 'sharabeya', 'wayli', 'kirdasah', 'mansura',
   'khalifah', 'mansheyet_nasser', 'giza_district',
   'alexandria_agriculture_road', 'middle_ring_road', 'makadi_bay',
   'marsa_alam', 'dabaa', 'attaka', 'suez_district']) 

    view = st.selectbox("View", ['back', 'seaview', 'View_of_Landmark',
   'View_of_Landmark + seawater', 'garden', 'main_street',
   'side_street', 'other', 'corner', 'pool', 'nile', 'golf', 'plaza',
   'club', 'lake']) 
    
    kind = st.selectbox("Kind", ['apartment', 'villa', 'chalet', 'penthouse', 'townhouse',
   'twin_house', 'duplex', 'room', 'furnished_apartment', 'land_farm',
   'building', 'residential_land', 'other_residential']) 
    
    categorical_columns = pd.DataFrame([[finish_type, city, district, view, kind]],columns = ['finish_type', 'city', 'district', 'view', 'kind'])
    
    cat__finish_type, cat__city, cat__district, cat__view, cat__kind = encoder.transform(categorical_columns)[0]
    if st.button("Predict"): 
        
        prediction = predict_house_price(
            int(room), int(bath), int(area), int(balcony), int(parking), int(maids_room),
       int(pets_allowed), int(gym), int(garden), int(kitchen_appliances), int(heating),
       int(elevator), int(natural_gas), int(security), int(water_meter), int(play_area),
       int(barbeque_area), int(CCTV), int(maintenance_staff), int(build_in), int(floor),
       int(cat__finish_type), int(cat__city) ,int(cat__district), int(cat__view),int(cat__kind)
        )
        
        st.success('{}'.format(prediction))
        
        
        

if __name__ == '__main__': 
    # Run Streamlit app
    main()