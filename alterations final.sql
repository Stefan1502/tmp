select * from copy_2015;
alter table copy_2015 
alter column datetime set data type timestamp        
using to_timestamp(datetime, 'DD-MM-YYYY HH24:MI');
alter table copy_2015 
alter column temperature set data type float8      
using temperature::double precision;
alter table copy_2015 
alter column humidity set data type float8      
using humidity::double precision;
alter table copy_2015 
alter column windspeed set data type float8      
using windspeed::double precision;
alter table copy_2015 
alter column data set data type float8      
using data::double precision;

select * from copy_2016;
alter table copy_2016 
alter column datetime set data type timestamp        
using to_timestamp(datetime, 'DD-MM-YYYY HH24:MI');
update copy_2016 set temperature=null where temperature='NULL';
alter table copy_2016
alter column temperature set data type float8      
using temperature::double precision;
update copy_2016 set humidity=null where humidity='NULL';
alter table copy_2016
alter column humidity set data type float8      
using humidity::double precision;
update copy_2016 set windspeed=null where windspeed='NULL';
update copy_2016 set percipitation =null where percipitation ='NULL';
alter table copy_2016 
alter column windspeed set data type float8      
using windspeed::double precision;

select * from copy_2017;
update copy_2017 set percipitation =null where percipitation ='NULL';
alter table copy_2017 
alter column datetime set data type timestamp        
using to_timestamp(datetime, 'DD-MM-YYYY HH24:MI');
alter table copy_2017
alter column data set data type float8      
using data::double precision;
alter table copy_2017
alter column temperature set data type float8      
using temperature::double precision;
alter table copy_2017
alter column humidity set data type float8      
using humidity::double precision;
alter table copy_2017
alter column windspeed set data type float8      
using windspeed::double precision;

select * from copy_2018;
alter table copy_2018 
alter column datetime set data type timestamp        
using to_timestamp(datetime, 'YYYY-MM-DD HH24:MI');
alter table copy_2018
alter column data set data type float8      
using data::double precision;
alter table copy_2018
alter column temperature set data type float8      
using temperature::double precision;
alter table copy_2018
alter column humidity set data type float8      
using humidity::double precision;
alter table copy_2018
alter column windspeed set data type float8      
using windspeed::double precision;

select * from copy_2019;
alter table copy_2019 
alter column datetime set data type timestamp        
using to_timestamp(datetime, 'YYYY-MM-DD HH24:MI');
alter table copy_2019
alter column data set data type float8      
using data::double precision;
alter table copy_2019 add column temperature float8;
alter table copy_2019 add column humidity float8;
alter table copy_2019 add column windspeed float8;
alter table copy_2019 add column percipitation text;

