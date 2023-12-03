/*
*--------------------------------------------------------------------

*File name: TVShow.cs

* Project name: Movie and TV Tracker

*--------------------------------------------------------------------

* Author’s name and email: Jericho McGowan || mcgowanj2@etsu.edu

* Course-Section: CSCI - 2910 - 001

* Creation Date: 11 / 24 / 2023

* -------------------------------------------------------------------
*/
namespace Movie_and_TV_Tracker.Data.Models
{
    public class TVShow
    {
        public int id { get; set; }
        public string name { get; set; }
        public string release_date { get; set; }
        public int number_of_episodes { get; set; }
        public string watch_status { get; set; }
    }
}
