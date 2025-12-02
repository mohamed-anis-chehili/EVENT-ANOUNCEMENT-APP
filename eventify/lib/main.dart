// import 'package:eventify/screens/home/home_screen.dart';
// import 'package:eventify/screens/favorite/favorite_screen.dart';
// import 'package:eventify/screens/profile/profile_screen.dart';
// import 'package:flutter/material.dart';
// import 'dart:ui';

// void main() {
//   runApp(const MainApp());
// }

// class MainApp extends StatefulWidget {
//   const MainApp({super.key});

//   @override
//   State<MainApp> createState() => _MainAppState();
// }

// class _MainAppState extends State<MainApp> {
//   int _selectedIndex = 0;

//   final List<Widget> _pages = const [
//     Home(),
//     // CalendarScreen(), // you can add it later
//     FavoritesScreen(),
//     ProfilePage(),
//   ];

//   void _onItemTapped(int index) {
//     setState(() {
//       _selectedIndex = index;
//     });
//   }

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       home: Scaffold(
//         body: _pages[_selectedIndex],
//         bottomNavigationBar: Container(
//           color: Colors.transparent,
//           child: Stack(
//             children: [
//               Positioned.fill(
//                 child: ClipRect(
//                   child: BackdropFilter(
//                     filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
//                     child: Container(color: Colors.transparent),
//                   ),
//                 ),
//               ),
//               Container(
//                 height: 60,
//                 width: double.infinity,
//                 margin: const EdgeInsets.only(left: 20, right: 20, bottom: 10),
//                 decoration: BoxDecoration(
//                   color: const Color.fromARGB(255, 35, 12, 51),
//                   borderRadius: BorderRadius.circular(30),
//                 ),
//                 child: Row(
//                   mainAxisAlignment: MainAxisAlignment.spaceEvenly,
//                   children: [
//                     IconButton(
//                       onPressed: () => _onItemTapped(0),
//                       icon: Icon(
//                         Icons.home_outlined,
//                         size: 30,
//                         color: _selectedIndex == 0 ? Colors.white : Colors.white54,
//                       ),
//                     ),
//                     IconButton(
//                       onPressed: () => {},
//                       icon: Icon(
//                         Icons.calendar_month,
//                         size: 30,
//                         color: _selectedIndex == 3 ? Colors.white : Colors.white54,
//                       ),
//                     ),
//                     IconButton(
//                       onPressed: () => _onItemTapped(1),
//                       icon: Icon(
//                         Icons.star_border_outlined,
//                         size: 30,
//                         color: _selectedIndex == 1 ? Colors.white : Colors.white54,
//                       ),
//                     ),
//                     IconButton(
//                       onPressed: () => _onItemTapped(2),
//                       icon: Icon(
//                         Icons.person_outline_outlined,
//                         size: 30,
//                         color: _selectedIndex == 2 ? Colors.white : Colors.white54,
//                       ),
//                     ),
//                   ],
//                 ),
//               ),
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }



