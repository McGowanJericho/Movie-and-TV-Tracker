/*
*--------------------------------------------------------------------

*File name: MovieInputObject.cs

* Project name: Movie and TV Tracker

*--------------------------------------------------------------------

* Author’s name and email: Jericho McGowan || mcgowanj2@etsu.edu

* Course-Section: CSCI - 2910 - 001

* Creation Date: 11 / 24 / 2023

* -------------------------------------------------------------------
*/
namespace Movie_and_TV_Tracker.Data.Models
{
    public class MovieInputObject
    {
        public string title { get; set; }
        public string release_date { get; set; }
        public int runtime_in_min { get; set; }
        public string watch_status { get; set; }
    }
}
