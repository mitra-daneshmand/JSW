import glob
import pandas as pd
import cv2
from utils import coordinates, jsw_lm, visualizing_landmarks

df_jsw = pd.DataFrame(columns=['ID', 'pixel_spacing', 'jsw_lat_left', 'jsw_med_left', 'jsw_lat_right', 'jsw_med_right'])

df = pd.read_excel(open('data/pixel_spacing.xlsx', 'rb'))
df = df.sort_values(by=['record_id'])
df = df.reset_index(drop=True)

points = sorted(glob.glob('data/points/' + '*.pts'))

for point in points:
    for row in range(len(df.index)):
        record_id = int(point[12:-4])
        if df['record_id'].iloc[row] == record_id:
            x, y = coordinates(point)

            # Visualizing the landmarks
            xray = cv2.imread('data/xrays/{}'.format(str(record_id) + '.jpeg'))
            visualizing_landmarks(xray, x, y)

            jsw_l_left, jsw_m_left, jsw_l_right, jsw_m_right = jsw_lm(x, y)

            jsw_l_left *= df['pixel_spacing'].iloc[row]
            jsw_m_left *= df['pixel_spacing'].iloc[row]
            jsw_l_right *= df['pixel_spacing'].iloc[row]
            jsw_m_right *= df['pixel_spacing'].iloc[row]

            df_jsw = df_jsw.append({'ID': record_id, 'pixel_spacing': df['pixel_spacing'].iloc[row],
                                    'jsw_lat_left': jsw_l_left.round(2), 'jsw_med_left': jsw_m_left.round(2),
                                    'jsw_lat_right': jsw_l_right.round(2), 'jsw_med_right': jsw_m_right.round(2)},
                                   ignore_index=True)
            continue

df_jsw.to_csv('JSW.csv', index=False)
