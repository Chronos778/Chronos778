import textwrap

left = '''
  maithil@github ~ [session: active]
 _________________________________________________________________
|                                                                 |
| $ whoami                                                        |
| _______________________________________________________________ |
||                                                               ||
||  Maithil - Aspiring Data Scientist                            ||
||  Problem Solver - Tech Enthusiast                             ||
||                                                               ||
||_______________________________________________________________||
|                                                                 |
| $ cat skills.json                                               |
|                                                                 |
| [languages]      JavaScript . Python . Java . C/C++             |
| [frontend]       React . Next.js                                |
| [backend]        Node.js . FastAPI                              |
| [databases]      PostgreSQL . MySQL . SQLite3                   |
| [tools]          Git . GitHub . Linux . VS Code                 |
|                                                                 |
| $ cat learning.txt                                              |
|                                                                 |
| > AI/ML                                                         |
|                                                                 |
| $ cat goals.txt                                                 |
|                                                                 |
| > Build scalable applications                                   |
| > Contribute to open source                                     |
| > Share knowledge with the community                            |
|                                                                 |
| $ _                                                             |
|_________________________________________________________________|
'''.strip('\n').split('\n')

right = r'''
                                      .._#%;*"_.:" ..
                                    _::*?*  .       :
                                   .::!          i   \.
                                 .!:.:, : .!      :   `:.
                               .i|]![.:*^I :  !   ! .:.  \
                              .#!!]!.[%.]:  :   ! : :.   ;
           .?!%.              .#%|.:!  [!*  ;!   !:. :+.+^'
          .P.*?'#:            ]iI! I.|.!.I |.  ! ."**:[%;
          '%::*#:.            .#'! I l'!!!.| |. .!' :.! %:#
             ..*=             .# ! l.l""|l.| .!' .: .!"%:#
              *i#           P.il |.*#?3#E"*"*"^?#%.! |!
                          I.d||.l.`##'|!!!:       '|I#.!Ji
                           #b..i[[l|I|.'b_j_.?*`      .-.:#i
                         .***..i[[l|I|.#E%#EP        *:?::#i
                    ....:J3|||I|I|I|I|E##E#.::" .      ..*#?
                  #"====================---*q3##E######E#" ;
                 !:.                          `%#E?"*?##E!.d||
                  %:.                           "P|!. J|*"..*^":
                   ":.                            ?#E#E#*+**"3#%:i
                     ':.    ._.                    "E## |__.f'|P?|
                       ':,    j#:                    ?##_ ..#i_ .!
                         ':,   "?b.'*.                 G?E#%##., .#|!
                           ':,                        'P|E#E?*]P##E
                             ':,                        !#E=*?##E?!
                               ':.
        #:::P#P?#E#===**#==*=*====*..*q.*#E######L.............3|E#E#i:.
        "**#===*#E##E#E#**#===*#=*#==#===*#E###E#E##=*#===*#===*E#E#E#Ei
'''.strip('\n').split('\n')

out = []
max_len = max(len(left), len(right))
for i in range(max_len):
    l = left[i] if i < len(left) else ' ' * 67
    r = right[i] if i < len(right) else ''
    l_padded = l.ljust(67)
    out.append(f'{l_padded}   {r}'.rstrip())

with open("scratch.txt", "w", encoding="utf-8") as f:
    f.write("```text\n")
    f.write('\n'.join(out))
    f.write("\n```")
