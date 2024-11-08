import pandas as pd

# from db_development import get_mysql_connection, get_sqlalchemy_engine
from db_production import get_mysql_connection, get_sqlalchemy_engine

# cek koneksi
try :
    connection = get_mysql_connection()
    engine = get_sqlalchemy_engine()
except Exception as e:
    print(e)


def update(latitude, longitude, id_pm):
    cursor = connection.cursor()
    try:
        query = ("""
                UPDATE tb_populasi_pm SET latitude = %s, longtitude = %s, flag_geocoding = %s WHERE id_populasi_pm = %s
            """)

        val = (latitude, longitude, 2, id_pm)
        cursor.execute(query, val)

        connection.commit()

    except Exception as e:
        connection.rollback()
        print("Failed to update into table : ", e)

def show():

    try:
        query = ("""
                    SELECT flag_geocoding, id_populasi_pm, main_mid_bri, main_mid_bni, main_mid_btn, main_mid_bmri,
                    main_mid_astrapay, main_mid,main_tid,main_mid_b,main_tid_b,main_nama_merchant, main_kota, main_alamat,
                    latitude,priority_pm,time_plan from tb_populasi_pm
                    ORDER BY priority_pm
                """)

        df = pd.read_sql(query, con=engine)
        if not df.empty:

            proses = 1
            for index, row in df.iterrows():
                print(f"ke-{proses} dengan id {row['id_populasi_pm']}")

                # your process here . . .

                proses += 1

    except Exception as e:
        print("Failed to display data : ", e)


# run
show()