import xarray as xr
import glob
path="./*out.nc"
df=[]

# append datasets into the list
for i in glob.glob(path, recursive=True):
    temp_df = xr.open_dataset(i)
    df.append(temp_df)
    #print(i,"----------")
  

df_final= 0

for i in range(len(df)):
   # print(df[i])
   # print(i,"-------------")
    df_final=df_final+df[i]
    

df_final.to_netcdf("combined_out.nc")
