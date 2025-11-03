class TopPicks {
  DateTime? date;
  String? nameOfevent;
  String? location;
  String? pathToImg;
  String? publisher;

  TopPicks(this.date, this.nameOfevent, this.pathToImg, this.location, this.publisher);
}

List<TopPicks> topPicks = [
  TopPicks(
    DateTime(11, 01, 2025),
    "Event 1",
    "lib/assets/event4.jpg",
    "ensia, Algiers",
    "Publisher",
  ),

  TopPicks(
    DateTime(11, 01, 2025),
    "Event 2",
    "lib/assets/event2.webp",
    "ensia, Algiers",
    "Publisher",
  ),

  TopPicks(
    DateTime(11, 01, 2025),
    "Event 3",
    "lib/assets/event3.webp",
    "ensia, Algiers",
    "Publisher",
  ),

  TopPicks(
    DateTime(11, 01, 2025),
    "Event 4",
    "lib/assets/event1.webp",
    "ensia, Algiers",
    "Publisher",
  ),
];
