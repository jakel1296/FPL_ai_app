# FPL AI — Data Sources & Field Reference

For the FPL AI project, data is separated into **official FPL player/team/fixture data** and **official Premier League/club team-news data**. The official FPL site now exposes a substantial amount of the information we need, including FDR, ownership, form and price-change information.

---

## 1. Official FPL bootstrap-static — player fields

Fields to retrieve from the official FPL API for every player.

| Exact field | What it means | Source |
|---|---|---|
| `id` | Unique FPL player ID | Official FPL bootstrap-static API |
| `first_name` | Player's first name | Official FPL bootstrap-static API |
| `second_name` | Player's surname/display name | Official FPL bootstrap-static API |
| `web_name` | FPL display name | Official FPL bootstrap-static API |
| `team` | Numeric ID of the player's current FPL team | Official FPL bootstrap-static API |
| `team_code` | Official club/team code | Official FPL bootstrap-static API |
| `element_type` | FPL position ID: GK/DEF/MID/FWD | Official FPL bootstrap-static API |
| `now_cost` | Current FPL price, in £0.1m units | Official FPL bootstrap-static API |
| `cost_change_start` | Price change since the start of the season (number/amount of price change from starting price) | Official FPL bootstrap-static API |
| `cost_change_event` | Price change during the current GW | Official FPL bootstrap-static API |
| `cost_change_start_fall` | Number of £0.1m price drops since GW1 | Official FPL bootstrap-static API |
| `cost_change_event_fall` | Number of £0.1m price drops in current GW | Official FPL bootstrap-static API |
| `total_points` | FPL points scored this season | Official FPL bootstrap-static API |
| `points_per_game` | Average FPL points per appearance/game | Official FPL bootstrap-static API |
| `form` | Recent FPL form | Official FPL bootstrap-static API |
| `selected_by_percent` | Percentage of FPL teams owning the player | Official FPL bootstrap-static API |
| `transfers_in` | Total transfers into the player | Official FPL bootstrap-static API |
| `transfers_out` | Total transfers out | Official FPL bootstrap-static API |
| `transfers_in_event` | Transfers in during current GW | Official FPL bootstrap-static API |
| `transfers_out_event` | Transfers out during current GW | Official FPL bootstrap-static API |
| `minutes` | Minutes played | Official FPL bootstrap-static API |
| `starts` | Number of starts | Official FPL bootstrap-static API |
| `appearances` | Number of appearances | Official FPL bootstrap-static API |
| `goals_scored` | Goals scored | Official FPL bootstrap-static API |
| `assists` | Assists | Official FPL bootstrap-static API |
| `clean_sheets` | Clean sheets | Official FPL bootstrap-static API |
| `goals_conceded` | Goals conceded while playing | Official FPL bootstrap-static API |
| `saves` | Goalkeeper saves | Official FPL bootstrap-static API |
| `penalties_saved` | Penalties saved | Official FPL bootstrap-static API |
| `penalties_missed` | Penalties missed | Official FPL bootstrap-static API |
| `yellow_cards` | Yellow cards | Official FPL bootstrap-static API |
| `red_cards` | Red cards | Official FPL bootstrap-static API |
| `own_goals` | Own goals | Official FPL bootstrap-static API |
| `bonus` | Bonus points earned | Official FPL bootstrap-static API |
| `bps` | Baseline Bonus Points System score | Official FPL bootstrap-static API |
| `influence` | FPL Influence metric | Official FPL bootstrap-static API |
| `creativity` | FPL Creativity metric | Official FPL bootstrap-static API |
| `threat` | FPL Threat metric | Official FPL bootstrap-static API |
| `ict_index` | Combined ICT score | Official FPL bootstrap-static API |
| `expected_goals` | Official FPL expected goals statistic | Official FPL bootstrap-static API |
| `expected_assists` | Official FPL expected assists statistic | Official FPL bootstrap-static API |
| `expected_goal_involvements` | xG + xA | Official FPL bootstrap-static API |
| `expected_goals_conceded` | Expected goals conceded | Official FPL bootstrap-static API |
| `value_form` | FPL's form-per-price metric | Official FPL bootstrap-static API |
| `value_season` | FPL's season-points-per-price metric | Official FPL bootstrap-static API |
| `ep_this` | FPL's expected-points/value metric | Official FPL bootstrap-static API |
| `ep_next` | FPL's next-GW expected-points metric | Official FPL bootstrap-static API |
| `status` | Player availability status | Official FPL bootstrap-static API |
| `news` | FPL injury/suspension/availability note | Official FPL bootstrap-static API |
| `news_added` | Timestamp associated with the latest player news | Official FPL bootstrap-static API |
| `chance_of_playing_next_round` | FPL estimated chance of playing next GW | Official FPL bootstrap-static API |
| `chance_of_playing_this_round` | FPL estimated chance of playing current GW | Official FPL bootstrap-static API |
| `code` | Official FPL player code | Official FPL bootstrap-static API |

**Important:** some of these are primarily useful as raw inputs rather than things we'll directly use in the recommendation. For example, `influence`, `creativity` and `threat` are available, but the stated preference is to prioritise underlying xG/xA/xGC rather than FPL's points-derived metrics.

---

## 2. Official FPL bootstrap-static — teams

| Exact field | What it means | Source |
|---|---|---|
| `id` | Unique FPL team ID | Official FPL bootstrap-static API |
| `name` | Club name | Official FPL bootstrap-static API |
| `short_name` | Three-letter/short club name | Official FPL bootstrap-static API |
| `code` | Official club code | Official FPL bootstrap-static API |
| `strength` | Overall FPL fixture-strength rating | Official FPL bootstrap-static API |
| `strength_overall_home` | Home strength rating | Official FPL bootstrap-static API |
| `strength_overall_away` | Away strength rating | Official FPL bootstrap-static API |
| `strength_attack_home` | Home attacking strength | Official FPL bootstrap-static API |
| `strength_attack_away` | Away attacking strength | Official FPL bootstrap-static API |
| `strength_defence_home` | Home defensive strength | Official FPL bootstrap-static API |
| `strength_defence_away` | Away defensive strength | Official FPL bootstrap-static API |

---

## 3. Official FPL fixtures

From the official FPL fixture endpoint we should retrieve:

| Exact field | What it means | Source |
|---|---|---|
| `id` | Unique fixture ID | Official FPL fixtures API |
| `event` | Gameweek number | Official FPL fixtures API |
| `team_h` | Home team ID | Official FPL fixtures API |
| `team_a` | Away team ID | Official FPL fixtures API |
| `team_h_score` | Home score, when played | Official FPL fixtures API |
| `team_a_score` | Away score, when played | Official FPL fixtures API |
| `finished` | Whether fixture has finished | Official FPL fixtures API |
| `kickoff_time` | Scheduled kickoff | Official FPL fixtures API |
| `minutes` | Fixture/minutes information | Official FPL fixtures API |
| `provisional_start_time` | Whether kickoff time is provisional | Official FPL fixtures API |
| `difficulty` | FPL's fixture difficulty rating | Official FPL fixtures API |
| `stats` | Player-level fixture statistics | Official FPL fixtures API |

This is particularly important for fixture run / FDR / rotation / DGW/BGW analysis.

---

## 4. Official FPL gameweek data

Gameweek/event information:

| Exact field | What it means | Source |
|---|---|---|
| `id` | Gameweek number | Official FPL bootstrap-static API |
| `name` | Gameweek name | Official FPL bootstrap-static API |
| `deadline_time` | Transfer deadline | Official FPL bootstrap-static API |
| `finished` | Whether GW has finished | Official FPL bootstrap-static API |
| `is_current` | Whether this is the current GW | Official FPL bootstrap-static API |
| `is_next` | Whether this is the next GW | Official FPL bootstrap-static API |
| `average_entry_score` | Average FPL score for the GW | Official FPL bootstrap-static API |
| `highest_score` | Highest GW score | Official FPL bootstrap-static API |
| `most_selected` | Most-selected player information | Official FPL bootstrap-static API |
| `most_transferred_in` | Most transferred-in player | Official FPL bootstrap-static API |
| `most_transferred_out` | Most transferred-out player | Official FPL bootstrap-static API |
| `highest_scoring_entry` | Highest-scoring team | Official FPL bootstrap-static API |

---

## 5. Official FPL price-change data

This deserves its own category because price farming is specifically part of the strategy.

The 2026/27 FPL site now has an official **Price Change Predictor** which tracks transfer activity and updates the progress towards price rises/falls every 15 minutes.

Retrieve/store:

| Field | What it means | Source |
|---|---|---|
| `now_cost` | Current player price | Official FPL API |
| `cost_change_event` | Price movement in current GW | Official FPL API |
| `cost_change_start` | Total price movement since GW1 | Official FPL API |
| `transfers_in_event` | Current-GW buying pressure | Official FPL API |
| `transfers_out_event` | Current-GW selling pressure | Official FPL API |
| `selected_by_percent` | Current ownership | Official FPL API |
| `price_change_progress` | Progress towards next price rise/fall | Official FPL Price Change Predictor |
| `predicted_progress` | Predicted progress towards price change | Official FPL Price Change Predictor |

The last two are **not** the same thing as a guaranteed price change; FPL explicitly describes the predictor as a guide, with the threshold assessed around 00:00 UK time.

---

## 6. Official Premier League / club sources — team news

These aren't FPL API fields, but they are part of the official-source layer:

| Field | What it means | Source |
|---|---|---|
| `availability_status` | Whether player is available | Official PL / club |
| `injury` | Confirmed injury information | Official club / PL |
| `injury_return_date` | Expected/confirmed return | Official club / PL |
| `suspension` | Suspension information | Official PL / club |
| `manager_quote` | Manager's comments regarding player | Official club |
| `expected_start` | Evidence regarding expected selection | Official club / PL |
| `minutes_expectation` | Evidence about likely playing time | Official club / PL |
| `rotation_risk` | Derived assessment from official information | Derived from official sources |
| `team_selection` | Confirmed starting XI once available | Official club / PL |

The important distinction: `expected_start`, `minutes_expectation` and `rotation_risk` are **our derived fields**, not official database fields.

---

## 7. What we deliberately get from Understat instead

Because the FPL AI skill explicitly requires Understat for underlying data, these are **not** fields the FPL API is treated as the authoritative source for:

- xG
- xA
- npxG
- npxG+xA
- shots
- key passes
- minutes used to contextualise underlying numbers
- team attacking xG
- team defensive xGA
- player underlying per-90 rates

The FPL API does provide xG/xA-related statistics, and the Premier League itself explains that xG/xA/xGI are part of the FPL statistics ecosystem. But for our model, Understat remains the canonical underlying-data source, so we avoid mixing methodologies.

---

## The resulting canonical data model

| Layer | Provides |
|---|---|
| **Official FPL API** | identity, price, ownership, FPL points, minutes, starts, fixtures, FDR, availability, transfers, official FPL xG/xA fields |
| **Official PL / club sources** | injuries, suspensions, manager comments, predicted/confirmed selection, team news |
| **Understat** | underlying attacking/defensive process: xG, xA, npxG, npxG+xA etc. |
| **Our derived fields** | minutes reliability, 90-minute likelihood, xG/90, xA/90, xGC/90, points/£, xG/£, fixture-adjusted projections, opportunity cost, price-rise probability interpretation, transfer recommendation and chip timing |

This gives a clean distinction between **raw official data → raw underlying data → our calculations/interpretation**, which is the recommended data architecture for the FPL AI project.