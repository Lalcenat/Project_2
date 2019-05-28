-- Create and use project_db
CREATE DATABASE project_db;
USE project_db;

-- Create tables for raw data to be loaded into
CREATE TABLE gdp (
  id INT PRIMARY KEY AUTO_INCREMENT,
  country_name TEXT,
  gdp_1996 DOUBLE,
  gdp_1997 DOUBLE,
  gdp_1998 DOUBLE,
  gdp_1999 DOUBLE,
  gdp_2000 DOUBLE,
  gdp_2001 DOUBLE,
  gdp_2002 DOUBLE,
  gdp_2003 DOUBLE,
  gdp_2004 DOUBLE,
  gdp_2005 DOUBLE,
  gdp_2006 DOUBLE,
  gdp_2007 DOUBLE,
  gdp_2008 DOUBLE,
  gdp_2009 DOUBLE,
  gdp_2010 DOUBLE,
  gdp_2011 DOUBLE,
  gdp_2012 DOUBLE,
  gdp_2013 DOUBLE,
  gdp_2014 DOUBLE,
  gdp_2015 DOUBLE,
  gdp_2016 DOUBLE
);

CREATE TABLE life_expectancy (
  id INT PRIMARY KEY AUTO_INCREMENT,
  country_name TEXT,
  lfe_1996 DOUBLE,
  lfe_1997 DOUBLE,
  lfe_1998 DOUBLE,
  lfe_1999 DOUBLE,
  lfe_2000 DOUBLE,
  lfe_2001 DOUBLE,
  lfe_2002 DOUBLE,
  lfe_2003 DOUBLE,
  lfe_2004 DOUBLE,
  lfe_2005 DOUBLE,
  lfe_2006 DOUBLE,
  lfe_2007 DOUBLE,
  lfe_2008 DOUBLE,
  lfe_2009 DOUBLE,
  lfe_2010 DOUBLE,
  lfe_2011 DOUBLE,
  lfe_2012 DOUBLE,
  lfe_2013 DOUBLE,
  lfe_2014 DOUBLE,
  lfe_2015 DOUBLE,
  lfe_2016 DOUBLE
);

Select * from life_expectancy;
