namespace Movie_and_TV_Tracker.Data.Models
{
    public class Movie
    {
          public int id { get; set; }
        public string title { get; set; }
        public string release_date { get; set; }
        public int runtime_in_min { get; set; }
        public string watch_status { get; set; }
    }
}
